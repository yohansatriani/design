from django.template.loader import get_template, render_to_string
from django.template import Template, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from design.forms import LoginForm

#design
def home(request):
    html = render_to_string('page-home.html', {'title': "Home", 'head': "Home"})
    return HttpResponse(html)

def old_login(request):
    html = render_to_string('login.html', {'title': "Login | falconet", 'head': "Login"})
    return HttpResponse(html)

def auth_login(request):
    form = LoginForm()
    html = render_to_string('page-login.html', {'title': "Login |  Now", 'head': "Login", 'form': form})
    return HttpResponse(html)