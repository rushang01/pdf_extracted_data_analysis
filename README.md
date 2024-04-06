# cis6930sp24-assignment2
# Norman PD Data Extraction README
## Developer Information
Name: Rushang Sunil Chiplunkar

# Assignment Description 
## Objective
The objective of this project was to extract, process, and analyze incident data from publicly available PDF reports. The goal was to augment this data with additional contextual information such as weather conditions at the time of the incidents, geographical data (geocode), the day of the week, and time of the day. Furthermore, the project aimed to rank incidents based on the frequency of their nature and location, providing insights into common incident types and hotspots within the area of interest.

## Tools and Technologies Used
- **Python**: Served as the primary programming language for data extraction, processing, and analysis.
- **PyMuPDF (fitz)**: Used for reading and extracting text from PDF documents.
- **OpenMeteo**: Utilized for fetching historical weather data based on incident dates and locations.
- **SQLite**: Employed as the database solution for storing and querying incident data.
- **Concurrent Futures**: Leveraged for parallel execution to enhance efficiency, particularly for geocode fetching and weather data retrieval.
- **Requests**: Used for making HTTP requests to external APIs for geocoding and weather data.
- **Pandas**: Aided in handling and analyzing data for the generation of weather codes based on incident times.
- **Argparse**: Utilized for parsing command-line arguments, allowing the script to be executed with various user-defined parameters.
- **Datetime and timedelta**: Used for manipulating dates and times, including converting incident times to a different timezone.
- **Geopy**: Used for geocoding addresses to latitude and longitude coordinates.

## Highlights and Learning Outcomes
- **Data Extraction from PDFs**: Gained experience in extracting structured data from unstructured PDF reports using PyMuPDF, navigating challenges associated with text layout and formatting.
- **Parallel Processing**: Implemented parallel processing techniques to improve the efficiency of real-time data fetching tasks, significantly reducing the time required for geocoding and weather data retrieval.
- **Weather Data Integration**: Integrated external weather data into the incident analysis, enhancing the dataset with contextual information that could influence incident analysis.
- **Geocoding and Geographical Analysis**: Learned to convert textual location data into geocoded coordinates and use these coordinates to determine the side of the town where incidents occurred, facilitating spatial analysis of incidents.
- **Data Ranking with Ties**: Developed a custom solution for ranking incident frequencies by nature and location, accounting for ties in the ranking process.
- **Database Management**: Gained hands-on experience with SQLite for data storage and retrieval, understanding the benefits of persisting processed data for future analysis.
- **API Interaction**: Improved skills in interacting with external APIs for geocoding and weather data, including handling API rate limits and responses.
- **Learning Outcome**: This project highlighted the importance of integrating diverse data sources to provide a more comprehensive analysis. It underscored the power of Python for data processing and analysis, and the use of databases and external APIs to enrich datasets. The project also reinforced best practices in code organization, modularization, and the use of version control for collaborative development.


# How to Install
To install and run this project, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have Python installed. This project was developed with Python 3.8.

## How to Use

To run the program, follow these steps to set up your environment and execute the program.

### Setting Up Your Environment

1. **Install Pipenv**:
   - Use the command below to install Pipenv if it's not already installed. Pipenv is a tool that helps manage virtual environments and package installations.
     ```bash
     pip install pipenv
     ```

2. **Install Dependencies**:
   - Navigate to your project's root directory and install the required dependencies with Pipenv by executing:
     ```bash
     pipenv install
     ```

3. **Activate the Virtual Environment**:
   - Activate the virtual environment created by Pipenv:
     ```bash
     pipenv shell
     ```

### Running the Program

- **Execute the Script**:
  - Run the following command to execute the program. Ensure to replace `files.csv` with your actual CSV file containing PDF URLs:
    ```bash
    pipenv run python assignment2.py --urls files.csv
    ```

### Running Test Cases

- **Test Execution**:
  - Execute the test cases with the following command:
    ```bash
    pipenv run python -m pytest
    ```

## Functions Description

### `augmentColummnWiseDataWithWeather(date_time_str, geocode)`
- **Purpose**: Fetches weather data based on a datetime string and geocode, adjusting the time for GMT+5.
- **How It Works**: Converts the input datetime string to a datetime object, adjusts this by 5 hours, and uses this adjusted datetime to fetch weather data. The weather code corresponding to the adjusted hour is returned.
- **Inputs**:
  - `date_time_str`: A string representing the datetime of an incident.
  - `geocode`: A list containing the latitude and longitude of the incident location. If the geocode is unknown, a default location (Norman, OK) is used.
- **Outputs**: A formatted weather code as a string or "Unknown" if data is not found.

### `calculate_bearing(center_lat, center_lon, lat, lon)`
- **Purpose**: Calculates the bearing from a central point to another latitude and longitude.
- **How It Works**: Uses trigonometry to calculate the bearing in degrees from the central point to the given latitude and longitude.
- **Inputs**:
  - `center_lat`, `center_lon`: The latitude and longitude of the central point.
  - `lat`, `lon`: The latitude and longitude of the target point.
- **Outputs**: The bearing in degrees as a float.

### `get_direction_from_bearing(bearing)`
- **Purpose**: Converts a bearing in degrees to a cardinal direction (e.g., N, NE, E, etc.).
- **How It Works**: Divides the bearing by 45 and rounds to find the index of the corresponding direction in a predefined list.
- **Inputs**:
  - `bearing`: The bearing in degrees.
- **Outputs**: A string representing the cardinal direction.

### `get_geocode_from_address(address)`
- **Purpose**: Fetches the geocode (latitude and longitude) for a given address.
- **How It Works**: Makes a request to the Google Maps Geocoding API with the address and parses the latitude and longitude from the response.
- **Inputs**:
  - `address`: The address to geocode.
- **Outputs**: A list containing the latitude and longitude or ["Unknown"] if the geocode cannot be determined.

### `determine_side_of_town(address, geocode, center)`
- **Purpose**: Determines the cardinal direction of an address from the center of town.
- **How It Works**: Uses the `calculate_bearing` function and then `get_direction_from_bearing` to determine the direction.
- **Inputs**:
  - `address`: The address to determine the side of town for.
  - `geocode`: The geocode of the address.
  - `center`: The latitude and longitude of the town's center.
- **Outputs**: A string representing the side of town (cardinal direction).

### `fetchincidents(url)`
- **Purpose**: Downloads a PDF from a given URL.
- **How It Works**: Makes an HTTP GET request to the specified URL and saves the response content as a PDF file.
- **Inputs**:
  - `url`: The URL of the PDF to download.
- **Outputs**: The file path to the downloaded PDF.

### `augmentColummnWiseDataWithDateAndTime(incident)`
- **Purpose**: Adds day of the week and hour of the day information to an incident record.
- **How It Works**: Parses the `date_time` attribute of an incident, calculates the day of the week and hour, and adds these as new attributes to the incident.
- **Inputs**:
  - `incident`: A dictionary representing an incident.
- **Outputs**: None. The function modifies the `incident` dictionary in place.

### `fetch_weather_for_incident(incident)`
- **Purpose**: Helper function for parallel fetching of weather data for an incident.
- **How It Works**: Calls `augmentColummnWiseDataWithWeather` for the provided incident.
- **Inputs**:
  - `incident`: A dictionary representing an incident, including `date_time` and `geocode`.
- **Outputs**: The weather code for the incident's datetime and location.

### `set_EMSSTAT_to_false(incident)`
- **Purpose**: Sets the `EMSSTAT` flag to false for an incident.
- **How It Works**: Modifies the `incident` dictionary to include an `EMSSTAT` key with a value of False.
- **Inputs**:
  - `incident`: A dictionary representing an incident.
- **Outputs**: None. The function modifies the `incident` dictionary in place.

### `rank_locations(incidents)`
- **Purpose**: Ranks incident locations by their frequency, preserving ties.
- **How It Works**: Counts occurrences of each location, sorts them by frequency, assigns ranks with ties accounted for, and updates each incident with its location rank.
- **Inputs**:
  - `incidents`: A list of dictionaries, each representing an incident.
- **Outputs**: None. The function modifies the `incidents` list in place, adding a `location_rank` to each incident.

### `rank_nature(incidents)`
- **Purpose**: Ranks the nature of incidents by their frequency, preserving ties.
- **How It Works**: Similar to `rank_locations`, but operates on the nature of incidents.
- **Inputs**:
  - `incidents`: A list of incident dictionaries.
- **Outputs**: None. Adds a `nature_rank` to each incident based on the frequency of its nature.

### `augmentColummnWiseData(incidents)`
- **Purpose**: Augments a list of incidents with additional data, including weather, side of town, and geocode.
- **How It Works**: Fetches geocodes in parallel, then adds weather data, side of town, and sets EMSSTAT flags.
- **Inputs**:
  - `incidents`: A list of incident dictionaries.
- **Outputs**: The augmented list of incidents.

### `extract_incidents_from_pdf(pdf_path)`
- **Purpose**: Extracts incident data from a given PDF file.
- **How It Works**: Opens a PDF and extracts text data to build a list of incident dictionaries.
- **Inputs**:
  - `pdf_path`: The file path of the PDF to process.
- **Outputs**: A list of incident dictionaries extracted from the PDF.

### `process_emsstat(incidents)`
- **Purpose**: Processes incidents to mark them with an EMSSTAT flag if applicable.
- **How It Works**: Iterates through incidents, marking related incidents with an EMSSTAT flag based on certain criteria.
- **Inputs**:
  - `incidents`: A list of incident dictionaries.
- **Outputs**: None. Modifies the `incidents` list in place, setting the `EMSSTAT` flag as needed.

### `handle_multiple_lines(columnWise_data, index, line)`
- **Purpose**: Handles the accumulation of text data into columns from PDF extraction.
- **How It Works**: Appends or sets text data to a specific index in a list, representing a column of data.
- **Inputs**:
  - `columnWise_data`: A list representing columns of data.
  - `index`: The index of the column to modify.
  - `line`: The text data to append or set.
- **Outputs**: None. Modifies the `columnWise_data` list in place.

### `print_incidents(incidents)`
- **Purpose**: Prints a summary of incidents to the console.
- **How It Works**: Iterates over the list of incidents, printing out selected attributes in a tab-separated format.
- **Inputs**:
  - `incidents`: A list of incident dictionaries.
- **Outputs**: None. Prints incident summaries to the console.

### `main(url, incidents)`
- **Purpose**: Main function to process a single URL and augment the list of incidents.
- **How It Works**: Downloads and extracts data from a PDF at the given URL, augments this data, and appends it to the provided list of incidents.
- **Inputs**:
  - `url`: The URL of a PDF to process.
  - `incidents`: A list of existing incident dictionaries to which new incidents will be added.
- **Outputs**: The updated list of incidents including those extracted from the specified URL.

### `process_urls(urls_file)`
- **Purpose**: Processes multiple URLs from a file, augmenting and printing incident data.
- **How It Works**: Reads URLs from a specified file, processes each URL in turn, and prints the augmented incident data.
- **Inputs**:
  - `urls_file`: The file path of a text file containing URLs, one per line.
- **Outputs**: None. Prints the augmented incident data to the console.



## Bugs and Assumptions

### Bugs
- **PDF Extraction Limitations**: The script relies heavily on the structure of the PDFs. If the format of the PDF changes significantly (e.g., different column layouts or added sections), the script may not accurately extract all data.
- **Geocode API Rate Limits**: The script may hit rate limits if processing a large number of incidents due to simultaneous geocode requests.
- **Weather Data Accuracy**: The script assumes weather data fetched based on the incident date and location accurately reflects the conditions at the time of the incident. Discrepancies may occur, especially for incidents occurring on the cusp of changing weather conditions.
- **Google Maps API Key Exposure**: If the API key is hardcoded within the script and the script is shared or made public, there's a risk of key exposure leading to unauthorized usage and potential cost implications.
- **Missing Data**: Specific details such as exact weather conditions and side of town had to be inferred from external sources and depend on whether the geocodes are generated for the respective locations or not. If the geocode is not generated for a particular location, the weather code and side of town are given a value of "Unknown".


### Assumptions
- **Stable PDF Format**: It is assumed that the PDFs have a consistent format where the incident data is organized in a predictable table-like structure across all documents.
- **Reliable Internet Connection**: The script assumes a stable and reliable internet connection for fetching geocode and weather data.
- **Accuracy of External APIs**: The script assumes that the geocoding and weather APIs provide accurate and up-to-date information.
- **Single Location Incidents**: The script assumes each incident report pertains to a single location - Norman, Oklahoma. Incidents spanning multiple locations may not be accurately represented.
- **Uniformity in Incident Reporting**: It is assumed that all incidents are reported with a similar level of detail and accuracy, allowing for uniform processing and analysis.
- **Handling of timezones**: The script utilizes an automated approach for time zone adjustments by setting the timezone parameter to "auto" within the API request. This means that the weather data fetched for each incident is automatically adjusted to match the local time zone based on the provided geolocation coordinates.
- **Geolocation Information**: When the script encounters an incident for which geolocation data (latitude and longitude) cannot be precisely determined due to limitations or failures in the geocoding process, it defaults to using the coordinates for Norman, Oklahoma (latitude = 35.2226, longitude = -97.4395). This decision ensures that weather data retrieval can still proceed by providing a fallback location, albeit with the implication that the weather data may not accurately represent the exact location of the incident if it occurred significantly outside this default area.