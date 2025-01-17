import requests


# endpoint ="https://httpbin.org/status/200/"
# endpoint ="https://httpbin.org/anything1234"
endpoint = "http://localhost:8000/api/"
get_response =requests.get(endpoint, params={"abc": 123}, json = {"query": "Hello there"}) # this defaults in the case the server does not respond

print(get_response.json())
# print(get_response.status_code)