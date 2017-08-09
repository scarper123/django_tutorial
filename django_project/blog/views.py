import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django import template

# Create your views here.


def index(request):
    return HttpResponse("Hello Django")


def today_is(request):
    now = datetime.datetime.now()
    # html = template.Template(
    #     '<html><body>Current date and time: {{ now|date:"Y" }}</body></html>')
    html = template.loader.get_template('blog/datetime.html')
    content = template.Context({"now": now})

    html = html.render(content)

    return HttpResponse(html)
