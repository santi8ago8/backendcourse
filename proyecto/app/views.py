# Create your views here.

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from datetime import datetime

from django.shortcuts import render_to_response


def hora_actual(request):
    '''
    ahora = datetime.now()
    t = get_template("hora.html")
    c = Context({"hora": ahora})
    html = t.render(c)

    return HttpResponse(html)
    '''
    now = datetime.now()
    return  render_to_response("hora.html",{'hora':now})