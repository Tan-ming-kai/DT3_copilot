from django.shortcuts import render


def landing(request):
    return render(request, 'landing.html')


def django_welcome(request):
    return render(request, 'django_welcome.html')

# Create your views here.
