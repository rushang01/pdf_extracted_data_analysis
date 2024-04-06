# Datasheets for Datasets - Augmented Incident Reports Dataset

## Motivation

- **For what purpose was the dataset created?**  
  The dataset was created as a part of cis6930sp24-assignment2, which is a data engineering assignment under CIS 6930 Spring 2024. After creation, an augmentation process was carried out that included enriching the dataset with additional context such as weather conditions, time categorizations, and geolocation interpretations to provide a more detailed analysis foundation.

- **Who created this dataset and on behalf of which entity?**  
  This dataset was created by Rushang Sunil Chiplunkar, a student of CIS 6930 Spring 2024, under the guidance of the course instructors.

- **Who funded the creation of the dataset?**  
  The augmentation process was an academic exercise, hence primarily supported by the University of Florida's resources allocated for educational purposes. Google Cloud credits provided for the assignment were used.

- **Any other comments?**  
  The augmented dataset is intended for academic use and for educational purposes, aiming to demonstrate how enriched data can support more nuanced analyses.

## Composition

- **What do the instances that comprise the dataset represent?**  
  Each instance reflects a police incident report, augmented with a weather code relevant to the incident's time and location. Incidents are categorized by hourly intervals, assigned a specific city quadrant based on their geographical coordinates, and given rankings based on the frequency of similar incident locations and natures.

- **How many instances are there in total?**  
  The number of instances depends upon on the number of incidents reported in the period under study. About 300-500 incidents can be expected.

- **Does the dataset contain all possible instances or is it a sample of instances from a larger set?**  
  The dataset includes all available incidents reported on the Norman Police Department's website for the specified time frame. The Norman Police Department updates their incident reports from time to time, so the code can only generate data for currently available incident PDFs on the Norman PD website.

- **What data does each instance consist of?**  
  Date/time, incident number, location, nature, and incident ORI. Augmented data includes weather conditions (WMO code), time of day (hour), location rank, side of town, and incident nature rank.

- **Is there a label or target associated with each instance?**  
  There is no target associated with each instance. the nature of the incident could be considered as the primary label.

- **Is any information missing from individual instances?**  
  Certain information may be missing from individual instances, with common ones being address and nature information.Specific details such as exact weather conditions and side of town had to be inferred from external sources and depend on whether the geocodes are generated for the respective locations or not. If the geocode is not generated for a particular location, the weather code and side of town are given a value of "Unknown".

- **Are relationships between individual instances made explicit (e.g., users’ movie ratings, social network links)?**  
  Not explicitly defined. However, one relationship is the boolean integer EMSSTAT, where if multiple incidents have the same date/time and occur at the same location, the EMSSTAT value is true for all of them. 

- **Are there recommended data splits (e.g., training, development/validation, testing)?**  
  Not applicable for this dataset as it is designed for comprehensive analysis rather than model training/testing.

- **Are there any errors, sources of noise, or redundancies in the dataset?**  
  Some degree of approximation was necessary for weather conditions and the side of town due to the the limitation of geocoding locations accurately.

- **Is the dataset self-contained, or does it link to or otherwise rely on external resources?**  
  Weather data was inferred using historical weather APIs based on the incidents' date and location. Geocoding API by Google was used to geocode locations. The entire dataset relies on the Norman PD website data.

- **Does the dataset contain data that might be considered confidential?**  
  The dataset does not include personal information. All data was publicly available through the Norman Police Department's website. 

- **Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety?**  
  The dataset does not contain sensitive personal data but does include incidents that might be distressing (e.g., domestic disturbances).

- **Does the dataset relate to people?**
  Yes, the dataset inherently relates to people as it consists of police incident reports involving individuals or groups. While the dataset is designed to focus on the incidents themselves—such as the nature of the call, location, time, and weather conditions—it indirectly involves human subjects due to the nature of law.

- **Does the dataset identify any subpopulations (e.g., by age, gender)?**  
  Not specifically identified. The dataset treats all incidents equally without segmentation by demographic groups.

- **Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset?**  
  It is not possible to identify individuals directly from this dataset. In combination with firsthand knowledge about the incident, it may be possible to identify individuals.

- **Does the dataset contain data that might be considered sensitive in any way (e.g., data that reveals racial or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history)?**  
  The content of the incidents may be viewed as delicate, yet the dataset prioritizes public safety information without disclosing any personal details.

## Collection Process

- **How was the data associated with each instance acquired?**  
  The data was directly observable, extracted from PDF summaries of daily incidents provided by the Norman Police Department, and augmented with additional context through external APIs for weather and geocoding, and some data manipulation with Python.

- **What mechanisms or procedures were used to collect the data?**  
  Data collection utilized Python scripts for PDF parsing, geocoding via Google Geocoding API, and weather data retrieval through the OpenMeteo API. For the side of town, bearing was calculated using Python's Math library.

- **Is the dataset a sample from a larger set?**  
  The dataset includes all available daily incident summaries for a specific timeframe, representing a comprehensive capture of reported incidents without sampling.

- **Who was involved in the data collection process?**  
  The dataset was collected by an individual student (Rushang Sunil Chiplunkar) without external compensation, relying on publicly available resources.

- **Over what timeframe was the data collected?**  
  Data was collected in real-time, corresponding to the daily release of incident summaries by the Norman Police Department.

- **Were any ethical review processes conducted?**  
  No formal ethical review was conducted, given the public nature of the data and its use for academic and research purposes.

## Preprocessing/Cleaning/Labeling

- **Was any preprocessing/cleaning/labeling of the data done?**  
  Yes. Parsing PDF texts, date and time parsing, geocoding, weather data retrieval, and categorizing incidents into sides of town.

- **Was the “raw” data saved in addition to the preprocessed/cleaned/labeled data?**  
  Raw data in the form of the PDF files provided by Norman PD is not saved, since it is publicly accessible.

- **Is the software used to preprocess/clean/label the instances available?**  
  Yes, the preprocessing scripts are available within the project repository. The pipfile contains all necessary libraries involved.

## Uses

- **Has the dataset been used for any tasks already?**  
  No, this dataset has not been used for any task yet. This project only involves creation of the dataset.

- **What (other) tasks could the dataset be used for?**  
  Besides analytical purposes, this dataset could serve as a foundational resource for various machine learning applications. It offers potential for developing predictive models that forecast incident likelihood based on temporal patterns, geographic locations, and meteorological conditions. Additionally, it could be instrumental in exploring correlations between incident types and specific weather conditions or times of day, facilitating more nuanced risk assessments. Researchers might also leverage the dataset for trend analysis over time, helping to identify emerging patterns or shifts in public safety concerns.

- **Is there anything about the composition of the dataset that might impact future uses?**  
  Users should consider potential biases in incident reporting and categorization. This dataset only uses data that was published by Norman PD, and cannot attest to fairness and bias factors relating to Norman PD data. Furthermore, it is important to consider the API limitations for this dataset. OpenMeteo API and Google Geocoding API can rate-limit your IP address after a certain number of requests. The time taken to run the script and generate the dataset is also extended by the use of these API's.

- **Are there tasks for which the dataset should not be used?**  
  The dataset should not be used for applications that could lead to privacy violations or misuse of the information for discriminatory purposes. 

## Distribution

- **How will the dataset be distributed?**  
  The dataset and its preprocessing scripts are distributed via GitHub to facilitate access and reproducibility.

- **Will the dataset be distributed under a copyright or other intellectual property (IP) license?**  
  The dataset is distributed under an open license permitting academic and research use.

- **When will the dataset be distributed?**
  Once the GitHub link is allowed to be public for the dataset. 

- **Will the dataset be distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)?**
  No.

- **Have any third parties imposed IP-based or other restrictions on the data associated with the instances?**
  No, since it is public data provided by Norman PD.

- **Do any export controls or other regulatory restrictions apply to the dataset or to individual instances?**
  No.

## Maintenance
- **Who will be supporting/hosting/maintaining the dataset?**  
  Ongoing support and updates will be provided by the dataset creator through GitHub.

- **How can the owner/curator/manager of the dataset be contacted?**  
  Via GitHub issues for questions, suggestions, or contributions to the dataset and preprocessing scripts.


- **If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so? If so, please provide a description. Will these contributions be validated/verified? If so, please describe how. If not, why not? Is there a process for communicating/distributing these contributions to other users? If so, please provide a description.**

  For individuals or entities interested in extending, augmenting, or contributing to the dataset, a structured process could be established to ensure consistency and quality. This process might involve submitting contributions via a designated online platform or repository, such as GitHub, where changes can be tracked and reviewed. However, such a process does not exist currently.

