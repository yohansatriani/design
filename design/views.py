from django.template.loader import get_template, render_to_string
from django.template import Template, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from design.forms import LoginForm

#design
def dummy(request):
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
def home(request):
    html = render_to_string('page-home.html', {'title': "Home", 'head': "Home", 'bcitems': ['home']})
    return HttpResponse(html)

def sites(request):
    html = render_to_string('page-sites.html', {'title': "Sites", 'head': "Sites", 'bcitems': ['home', 'sites']})
    return HttpResponse(html)

def auth_login(request):
    form = LoginForm()
    return render(request, 'page-login.html', {'title': "Login", 'head': "Login", 'form': form})

def old_login(request):
    html = render_to_string('login.html', {'title': "Login | falconet", 'head': "Login"})
    return HttpResponse(html)
