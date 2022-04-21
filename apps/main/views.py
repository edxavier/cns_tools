from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, 'home.html', locals())


def verification_view(request, *args, **kwargs):
    import time
    time.sleep(5)
    return render(request, 'host_verification.html', locals())