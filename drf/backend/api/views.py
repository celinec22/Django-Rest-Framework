import json
from django.http import JsonResponse

def api_home(request, *arges, **kwargs):
    # request -> HttpRequest -> Django
    print(request.GET) # url Query params
    body = request.body #byte string of json data
    data= {}
    try:
        data = json.loads(body) #string of json data -> python dictionary
    except:
        pass
    print(data)
    data['headers']= dict(request.headers)
    data['content_type']= request.content_type
    data['params']= dict(request.GET)

    return JsonResponse(data)