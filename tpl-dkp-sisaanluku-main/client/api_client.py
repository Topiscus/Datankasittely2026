# TODO: 
# Import requests library
# Define fetch_data function, that takes an API URL as parameter
# Use try - except structure to
# - make a GET request to the given URL with athe requests library,
# - raise an exception if the response status code indicates an error,
# - return the response data as JSON
# - print an error message if something goes wrong with the request, and return None.

import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/posts")

def fetch_data(url):
    try:    
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        response.raise_for_status() 
        return response.json()
    
    except requests.ConnectionError:
        print("Could not connect to the API.")

    except requests.exceptions.HTTPError as e:
        status = e.response.status_code if e.response is not None else "unknown"
        print(f"HTTP error: {status} - {e}")
    
    except json.JSONDecodeError:
        print("The server returned invalid JSON.")



