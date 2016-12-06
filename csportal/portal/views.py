from django.shortcuts import render
from user.models import Student


def home(request):
    return render(request, 'portal/home.html')


def about(request):
    return render(request, 'portal/about.html')
    
def show_all_students(request):

     return render(request, 'portal/showstudents.html', {'students' : Student.objects.all()})
    
