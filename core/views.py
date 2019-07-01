from django.shortcuts import render
from datetime import date
from django.core.mail import EmailMessage
from .forms import *
import time
import smtplib
from . import config


def home(request):
    localtime = time.asctime(time.localtime(time.time()))
    year = int(date.today().year)

    context = {
        'year': year,
        'localtime': localtime,
    }

    return render(request, 'core/home.html', context)


def about(request):

    edad = int(date.today().year)-1995
    exp = int(date.today().year)-2017
    year = int(date.today().year)
    localtime = time.asctime(time.localtime(time.time()))

    context = {
        'edad': edad,
        'exp': exp,
        'year': year,
        'localtime': localtime,
    }

    return render(request, 'core/about.html', context)


def contact(request):

    year = int(date.today().year)
    localtime = time.asctime(time.localtime(time.time()))
    form = Contact(request.POST or None)
    context = {
        'year': year,
        'localtime': localtime,
        'form': form,
    }

    if form.is_valid():
        context = {
            'form': form,
        }
        First_name = form.cleaned_data.get("First_name")
        Last_name = form.cleaned_data.get("Last_name")
        Email = form.cleaned_data.get("Email")
        Phone_number = form.cleaned_data.get("Phone_number")

        title = 'Client: ' + First_name + ' ' + Last_name
        body = First_name + ' ' + Last_name + ' ' + Email + ' ' + Phone_number + '\n\n  © 2019 · Diego Porro (Ingeniero Informatico)'

        print(title, body)

        email = EmailMessage(title, body, to=['diegoporro25@gmail.com'])
        email.send()
        form = Contact

    return render(request, 'core/contact.html', context)


def portfolio(request):

    year = int(date.today().year)
    localtime = time.asctime(time.localtime(time.time()))

    context = {
        'year': year,
        'localtime': localtime,
    }

    return render(request, 'core/prueba.html', context)
