from django.http import HttpResponse
import datetime
from django.shortcuts import render_to_response
from django.template import Template, Context
import os
SITE_ROOT = os.path.dirname(os.path.dirname(__file__))

def hello(request):
    return HttpResponse("Hello world")


def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('mytemplate.html', {'nows': now})



def hour_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError as e:
        raise Http404()

    time = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In {} hour(s), it will be {}.</body></html>".format(
        offset, time)
    return HttpResponse(html)
