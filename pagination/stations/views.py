from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv
import requests


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open('data-398-2018-08-30.csv', encoding='utf8') as f:
        content_list = []
        for row in csv.DictReader(f):
            content_list.append({'Name':row.get('Name'), 'Street':row.get('Street'), 'District':row.get('District')})
        page_number = int(request.GET.get('page', 1))
        paginator = Paginator(content_list, 10)
        page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
