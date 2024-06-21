import socket
from django.http import HttpResponse


def get_hostname(request):
    hostname = socket.gethostname()
    return HttpResponse(f"hello from the {hostname}")
