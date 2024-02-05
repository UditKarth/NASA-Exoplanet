# Exoplanet Query Web Application
## Overview
This web application allows users to query the Exoplanet Archive using the Table Access Protocol (TAP). It is built with Flask, a Python web framework, and utilizes Pandas for data manipulation. Users can input various search criteria to retrieve data about exoplanets, such as star name, discovery year, planet radius, distance in parsecs, and planet name. **Based on project idea from https://github.com/florinpop17/app-ideas/blob/master/Projects/3-Advanced/NASA-Exoplanet-Query.md**

## Installation

### Prerequisites
- Python 3.6 or later

### Dependencies
- Flask
- Pandas
- Requests

### Steps
1. Clone the repository
```
https://github.com/UditKarth/NASA-Exoplanet.git
cd exoplanet-query
```

2. Install required packages 
```
pip install flask pandas requests
```

3. Start the flask server and enjoy!
```
python main.py
```

### How to Use
1. Start the flask server using the above command

2. Open a web browser and navigate to http://localhost:5000/.

3. Use the form on the webpage to enter query parameters for exoplanets.

4. Submit the form to view the query results, which will be displayed on a new page.

### Features
Query the Exoplanet Archive dynamically based on user input.
Flexible search options including star name, discovery year, planet radius, and more.
Results are presented in a user-friendly tabular format.
