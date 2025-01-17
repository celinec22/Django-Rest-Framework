import requests

# Define the API endpoint
endpoint = "http://localhost:8000/api/"

# Send a GET request with query parameters and JSON body.
get_response = requests.get(
    endpoint,
    params={"abc": 123},  # Query parameters
    json={"query": "Hello there"}  # JSON body
)

# Print the JSON response from the server.
print(get_response.json())