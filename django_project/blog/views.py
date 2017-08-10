import datetime

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello Django")


def today_is(request):
    now = datetime.datetime.now()
    # html = template.Template(
    #     '<html><body>Current date and time: {{ now|date:"Y" }}</body></html>')
    # html = template.loader.get_template('blog/datetime.html')
    # content = template.Context({"now": now})

    # html = html.render({"now": now})

    # return HttpResponse(html)

    return render(request, 'blog/datetime.html', 
        {"now": now, "nav": "blog/nav.html"})
