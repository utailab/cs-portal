from django.shortcuts import render
from user.models import Student


def home(request):
    return render(request, 'portal/home.html')


def about(request):
    return render(request, 'portal/about.html')
    
def users(request):
     return render(request, 'portal/users.html', {'students' : Student.objects.all()})
    
