from django.shortcuts import render
from .models import Project
from datetime import date
import time

# Create your views here.


def portfolio(request):
    projects = Project.objects.all()

    year = int(date.today().year)
    localtime = time.asctime(time.localtime(time.time()))

    context = {
        'year': year,
        'localtime': localtime,
        'projects': projects,
    }

    return render(request, 'portfolio/portfolio.html', context)
