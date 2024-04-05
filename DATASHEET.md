# Datasheets for Datasets - Augmented Incident Reports Dataset

## Motivation

- **For what purpose was the dataset created?**  
  The dataset was augmented to enhance the usability of public safety data from the Norman Police Department for predictive modeling, trend analysis, and comprehensive public safety studies. The augmentation process included enriching the dataset with additional context such as weather conditions, time categorizations, and geolocation interpretations to provide a more detailed analysis foundation.

- **Who created this dataset and on behalf of which entity?**  
  This dataset was augmented by the students of CIS 6930 Spring 2024, under the guidance of the course instructors.

- **Who funded the creation of the dataset?**  
  The augmentation process was an academic exercise, hence primarily supported by the University of Florida's resources allocated for educational purposes.

- **Any other comments?**  
  The augmented dataset is intended for academic use, aiming to demonstrate how enriched data can support more nuanced analyses in public safety research.

## Composition

- **What do the instances that comprise the dataset represent?**  
  Each instance represents a police incident report, augmented with weather conditions at the incident's time and location, the incident's time categorized into hour blocks, a derived side of town based on the incident's geographical location, and rankings based on the frequency of incident locations and natures.

- **How many instances are there in total?**  
  To be determined based on the number of incidents reported in the period under study.

- **Does the dataset contain all possible instances or is it a sample of instances from a larger set?**  
  The dataset includes all available incidents reported on the Norman Police Department's website for a given time frame.

- **What data does each instance consist of?**  
  "Raw data includes date/time, incident number, location, nature, and ORI. Augmented data includes weather conditions (WMO code), time of day (hour), location rank, side of town, and incident nature rank."

- **Is there a label or target associated with each instance?**  
  Each instance's primary label is the nature of the incident, with additional contextual labels added through data augmentation.

- **Is any information missing from individual instances?**  
  No systemic information is missing from the instances; however, specific details such as exact weather conditions had to be inferred from external sources.

- **Are relationships between individual instances made explicit (e.g., users’ movie ratings, social network links)?**  
  Not explicitly defined beyond the augmentation that adds context to each incident.

- **Are there recommended data splits (e.g., training, development/validation, testing)?**  
  Not applicable for this dataset as it is designed for comprehensive analysis rather than model training/testing.

- **Are there any errors, sources of noise, or redundancies in the dataset?**  
  Some degree of approximation was necessary for weather conditions and the side of town due to the nature of the available data.

- **Is the dataset self-contained, or does it link to or otherwise rely on external resources?**  
  Weather data was inferred using historical weather APIs based on the incidents' date and location.

- **Does the dataset contain data that might be considered confidential?**  
  The dataset does not include personal information. All data was publicly available through the Norman Police Department's website.

- **Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety?**  
  The dataset does not contain sensitive personal data but does include incidents that might be distressing (e.g., domestic disturbances).

- **Does the dataset identify any subpopulations (e.g., by age, gender)?**  
  Not specifically identified; the dataset treats all incidents equally without segmentation by demographic groups.

- **Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset?**  
  It is not possible to identify individuals from this dataset.

- **Does the dataset contain data that might be considered sensitive in any way (e.g., data that reveals racial or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history)?**  
  The nature of the incidents might be considered sensitive; however, the dataset focuses on public safety without revealing personal data.

## Collection Process

### Data Acquisition
- **How was the data associated with each instance acquired?**  
  The data was directly observable, derived from PDF summaries of daily incidents provided by the Norman Police Department, and enriched with additional context through external APIs for weather and geocoding.

### Collection Mechanisms
- **What mechanisms or procedures were used to collect the data?**  
  Data collection utilized Python scripts for PDF parsing, geocoding via Google Maps API, and weather data retrieval through the OpenMeteo API.

### Sampling Strategy
- **Is the dataset a sample from a larger set?**  
  The dataset includes all available daily incident summaries for a specific timeframe, representing a comprehensive capture of reported incidents without sampling.

### Data Collection Personnel and Compensation
- **Who was involved in the data collection process?**  
  The dataset was collected by an individual researcher without external compensation, relying on publicly available resources.

### Timeframe of Data Collection
- **Over what timeframe was the data collected?**  
  Data was collected in real-time, corresponding to the daily release of incident summaries by the Norman Police Department.

### Ethical Review
- **Were any ethical review processes conducted?**  
  No formal ethical review was conducted, given the public nature of the data and its use for academic and research purposes.

## Preprocessing/Cleaning/Labeling

### Preprocessing Steps
- **Was any preprocessing/cleaning/labeling of the data done?**  
  Yes, preprocessing included parsing PDF texts, date and time parsing, geocoding, weather data retrieval, and categorizing incidents into sides of town.

### Raw Data Preservation
- **Was the “raw” data saved in addition to the preprocessed/cleaned/labeled data?**  
  Yes, raw data in the form of original PDF files and retrieved API responses was preserved.

### Preprocessing Software Availability
- **Is the software used to preprocess/clean/label the instances available?**  
  Yes, the preprocessing scripts are available within the project repository.

## Uses

### Previous Uses
- **Has the dataset been used for any tasks already?**  
  The dataset has been used to analyze police incident reporting patterns, including time-based trends and geographical distribution.

### Potential Tasks
- **What (other) tasks could the dataset be used for?**  
  Beyond analysis, the dataset could support machine learning tasks like predictive modeling of incidents based on time, location, and weather conditions.

### Impact on Future Uses
- **Is there anything about the composition of the dataset that might impact future uses?**  
  Users should consider potential biases in incident reporting and categorization. Fair and ethical use guidelines are recommended to mitigate biases.

### Restrictions on Use
- **Are there tasks for which the dataset should not be used?**  
  The dataset should not be used for applications that could lead to privacy violations or misuse of the information for discriminatory purposes.

## Distribution

### Distribution Plans
- **How will the dataset be distributed?**  
  The dataset and its preprocessing scripts are distributed via GitHub to facilitate access and reproducibility.

### Licensing
- **Will the dataset be distributed under a copyright or other intellectual property (IP) license?**  
  The dataset is distributed under an open license permitting academic and research use, with attribution and non-commercial restrictions.

## Maintenance

### Support and Maintenance
- **Who will be supporting/hosting/maintaining the dataset?**  
  Minimal ongoing support and updates will be provided by the dataset creator through GitHub.

### Contact Information
- **How can the owner/curator/manager of the dataset be contacted?**  
  Via GitHub issues for questions, suggestions, or contributions to the dataset and preprocessing scripts.

## Ethical Considerations

### Google Maps API Key
- **Discussion on the use of Google Maps API key**  
  The geocoding functionality relies on the Google Maps API. Users are advised to use their own API key and comply with Google's terms of service, especially regarding data privacy and usage limits.
