from django.shortcuts import render
from .host_definitions import operational
from core import net
# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, 'home.html', locals())


def verification_view(request, *args, **kwargs):
    for host in operational:
        has_ping = net.ping(host_ip=host.get('ip', ''))
        print(f"{host.get('app')} has ping {has_ping}")
    return render(request, 'host_verification.html', locals())