from django.shortcuts import render

from . import models


def profile(request, username=None):
    context = {}
    student = models.Student.objects.get(user__username=username)
    context['student'] = student
    return render(request, 'user/profile.html', context)
