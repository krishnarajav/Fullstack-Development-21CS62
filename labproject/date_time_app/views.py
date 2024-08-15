from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta

def current_datetime(request):
    now = datetime.now()
    html = f"<html><body><h1>Current Date and Time:</h1><p>{now}</p></body></html>"
    return HttpResponse(html)

def current_datetime_with_offset(request, offset):
    now = datetime.now()
    future_time = now + timedelta(hours=offset)
    past_time = now - timedelta(hours=offset)
    response = f"Current Date and Time: {now}<br>"
    response += f"Future Date and Time (+{offset} hours):{future_time}<br>"
    response += f"Past Date and Time (-{offset} hours):{past_time}"
    return HttpResponse(response)

