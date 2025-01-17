from django.http import JsonResponse

def api_home(request, *arges, **kwargs):
    return JsonResponse({"message": "Hi there, this is your django API Response!"})