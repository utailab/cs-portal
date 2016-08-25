from django.shortcuts import render


def home(request):
    return render(request, 'portal/home.html')

def about(request):
    return render(request, 'portal/about.html')
