import argparse
from concurrent.futures import ThreadPoolExecutor
import re
import urllib.request
import os
import fitz

from augment_rank import rank_locations, rank_nature
from date_and_time import augmentColummnWiseDataWithDateAndTime
from emsstat import process_emsstat, set_EMSSTAT_to_false
from geocoding import get_geocode_from_address
from side_of_town import determine_side_of_town
from weather import fetch_weather_for_incident
 

def fetchincidents(url):
    """
    Download the PDF from the given URL and return the file path.
    """
    response = urllib.request.urlopen(url)
    file_name = os.path.join('/tmp', 'incident.pdf')
    with open(file_name, 'wb') as file:
        file.write(response.read())
    return file_name


def augmentColummnWiseData(incidents):

    addresses = [incident["location"] for incident in incidents]

    with ThreadPoolExecutor(max_workers=10) as executor:
        geocodes = list(executor.map(get_geocode_from_address, addresses))

     # Update incidents with geocodes
    for incident, geocode in zip(incidents, geocodes):
        incident["geocode"] = geocode

    # Augment each incident with date and time first
    for incident in incidents:
        augmentColummnWiseDataWithDateAndTime(incident)
        set_EMSSTAT_to_false(incident)

    # Use ThreadPoolExecutor to fetch weather data in parallel
    with ThreadPoolExecutor(max_workers=10) as executor:
        weather_results = list(executor.map(fetch_weather_for_incident, incidents))


    # Augment incidents with fetched weather data and determine the side of town
    for incident, weather_code in zip(incidents, weather_results):
        incident["weather"] = weather_code
        incident["side_of_town"] = determine_side_of_town(incident["location"], incident["geocode"])

    incidents = process_emsstat(incidents)
    return incidents


def extract_incidents_from_pdf(pdf_path):

    colStartCoordinates = [52.560001373291016,150.86000061035156,229.82000732421875,423.19000244140625,623.8599853515625]
    columnWise_data = ["","","","",""]
  

    pdf_document = fitz.open(pdf_path)
    incidents = []
    i = 0
    for page in pdf_document:
        previousLineId = 0 #A line can be date+time, address, etc
        previousBlockId = 1
        words = page.get_text("words")
        if i == 0:
            words = words[9:-7]
            i+=1
        if i == len(pdf_document) - 1:
            words = words[:-2]
        #This is done to append a word to the end of the list of words. 
        #If this isn't done, the last word of each page would be missing, since I always operate on the subsequent word in this code.
        words = words +[words[0]]

        
        line = ""
        x = 0
        #(0:x0, 1:y0, 2:x1, 3:y1, 4:"word", 5:block_no, 6:line_no, 7:word_no)
        for word in words:
            if previousLineId == word[6]:
                if word[7] == 0:
                    line = word[4]
                    x = word[0]
                else:
                    line = line + " " + word[4] 
            
            else:
                for index,colstartCoordinate in enumerate(colStartCoordinates):
                    if index < len(colStartCoordinates)-1:
                        if x < colStartCoordinates[index+1] and x >= colStartCoordinates[index]:
                            handle_multiple_lines(columnWise_data,index,line)
                            
                    if index == len(colStartCoordinates)-1 and x >= colStartCoordinates[index]:
                            handle_multiple_lines(columnWise_data,index,line)
                line = word[4]
                x = word[0]
                previousLineId = word[6]

            if word[5] != previousBlockId:
                incident = {
                         "date_time": columnWise_data[0],
                         "incident_number": columnWise_data[1],
                         "location": columnWise_data[2],
                         "nature": columnWise_data[3],
                         "incident_ori": columnWise_data[4]
                     }
                columnWise_data = ["","","","",""]
                incidents.append(incident)
                previousBlockId = word[5]
   
    pdf_document.close()
    # Filter out incidents with no set values
    incidents = [incident for incident in incidents if any(incident.values())]
    return incidents


def handle_multiple_lines(columnWise_data,index,line):
    if columnWise_data[index]:
        columnWise_data[index] = columnWise_data[index] + " " + line
    else:
        columnWise_data[index] = line

def print_incidents(incidents):
    
    for incident in incidents:
        # Extract the required information from each incident
        day_of_week = incident.get("day", "Unknown")
        time_of_day = incident.get("hour", "Unknown")  
        weather = incident.get("weather", "Unknown")
        location_rank = incident.get("location_rank", "Unknown")
        side_of_town = incident.get("side_of_town", "Unknown")
        nature_rank = incident.get("nature_rank", "Unknown")  
        nature = incident.get("nature", "Unknown")
        emsstat = incident.get("EMSSTAT", False) 

        # Format the information as a tab-separated string
        incident_str = f"{day_of_week}\t{time_of_day}\t{weather}\t{location_rank}\t{side_of_town}\t{nature_rank}\t{nature}\t{int(emsstat)}"
        
        # Print the formatted string
        print(incident_str)


def main(url,incidents):
    # Download data
    incident_data = fetchincidents(url)

    # Extract data
    new_incidents = extract_incidents_from_pdf(incident_data)
    
    #Augment data
    new_incidents = augmentColummnWiseData(new_incidents)

    return incidents + new_incidents


def process_urls(urls_file):

    incidents = []

    #Process urls
    with open(urls_file, 'r') as file:
        urls = file.read()

    urls = re.split(',|\n', urls) 
    
    for url in urls:
        if url:
            incidents = main(url,incidents)

    rank_locations(incidents)
    rank_nature(incidents)
    
    print_incidents(incidents)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--urls", type=str, required=True, help="File containing incident summary URLs.")
    args = parser.parse_args()

    if args.urls:
       process_urls(args.urls)