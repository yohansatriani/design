from django.template.loader import get_template, render_to_string
from django.template import Template, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

#design
def login(request):
    html = render_to_string('login.html', {'title': "Login | falconet", 'head': "Login"})
    return HttpResponse(html)

def nowlogin(request):
    html = render_to_string('now-login.html', {'title': "Login |  Now", 'head': "Login Now"})
    return HttpResponse(html)