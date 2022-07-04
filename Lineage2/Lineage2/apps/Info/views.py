from django.shortcuts import render
from .models import Info
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'Info/Info.html', {'Info': Info.about_us,
                                              'Photo': Info.photo})