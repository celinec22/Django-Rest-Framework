import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    # `request` is the HttpRequest object passed to the view.
    print(request.GET)  # Logs query parameters in the console, e.g., `?abc=123`.
    
    body = request.body  # The raw byte string of the request's body.
    data = {}  # Initialize an empty dictionary to store response data.
    
    try:
        data = json.loads(body)  # Parse the body (JSON) into a Python dictionary.
    except:
        pass  # If parsing fails (e.g., no JSON body), just skip it.

    print(data)  # Logs the parsed body (if any).

    # Add additional information to the response data.
    data['headers'] = dict(request.headers)  # Include request headers.
    data['content_type'] = request.content_type  # Include content type.
    data['params'] = dict(request.GET)  # Include query parameters.

    return JsonResponse(data)  # Return the response as JSON.
