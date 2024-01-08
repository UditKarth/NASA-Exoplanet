from flask import Flask, render_template, request
from scrape import new_scrape, dataframe_to_jsonfile

app = Flask(__name__)
BASE_URL = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query="

def query_exoplanets(params):
# Constructing the where clause based on params
    conditions = []
    if params.get("star_name"):
        conditions.append(f"hostname like '%{params['star_name']}%'")
    if params.get("discovery_year"):
        conditions.append(f"disc_year = {params['discovery_year']}")
    if params.get("planet_radius_min") and params.get("planet_radius_max"):
        conditions.append(f"pl_rade between {params['planet_radius_min']} and {params['planet_radius_max']}")
    if params.get("distance_min") and params.get("distance_max"):
        conditions.append(f"sy_dist between {params['distance_min']} and {params['distance_max']}")
    if params.get("planet_name"):
        conditions.append(f"pl_name like '%{params['planet_name']}%'")
    if conditions:
        query += " where " + " and ".join(conditions)

    # Specify the format (e.g., CSV)
    query += "&format=csv"

    # Construct full URL
    full_url = BASE_URL + query.replace(" ", "+")

    # Make a request to the TAP service
    response = requests.get(full_url)
    if response.status_code == 200:
        return response.text
    else:
        return f"Error: {response.status_code}"

@app.route('/')
def index():
    return render_template('index.html')  # A form for user input

@app.route('/query', methods=['POST'])
def query():
    # Extract form data
    query_params = {
        "star_name": request.form.get('starName'),
        "discovery_year": request.form.get('discoveryYear'),
        "planet_radius_min": request.form.get('planetRadiusMin'),
        "planet_radius_max": request.form.get('planetRadiusMax'),
        "distance_min": request.form.get('distanceMin'),
        "distance_max": request.form.get('distanceMax'),
        "planet_name": request.form.get('planetName'),
        # Add other form parameters as needed
    }

    # Use the query_exoplanets function to fetch data
    data = query_exoplanets(query_params)

    # Convert the data to a suitable format for rendering, if necessary
    # For example, if data is in CSV format, convert it to a list of dictionaries

    # Display results
    return render_template('results.html', data=data)