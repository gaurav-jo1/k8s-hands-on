import socket
from django.http import HttpResponse
import requests

def get_hostname(request):
    hostname = socket.gethostname()
    return HttpResponse(f"Version 2: Hello from the {hostname}")

def get_nginx(request):
    url = "https://nginx"
    response = requests.get(url)
    return HttpResponse(response)
