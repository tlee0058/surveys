# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import strftime, gmtime
# Create your views here.
def index(request):
    return render(request, "session_words/index.html")

def add_words(request):
    if request.method == "POST":
            
            request.session['desc'] = request.POST['desc']
            context = {
                "time" : strftime("%b %d, %Y  %H:%M %p", gmtime()),
            }
            
            
            return render(request, "session_words/index.html", context)

    else:
        return redirect(index)
