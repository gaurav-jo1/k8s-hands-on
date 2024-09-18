import socket
from django.http import HttpResponse


def get_hostname(request):
    hostname = socket.gethostname()
    return HttpResponse(f"Version 2: Hello from the {hostname}\n")
