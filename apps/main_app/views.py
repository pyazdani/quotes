# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User, Quote
from django.contrib import messages

def index(request):
    return render(request, "main_app/index.html")

def new_user(request):
    user = User.userManager.register(
        request.POST['name'],
        request.POST['username'],
        request.POST['password'],
        request.POST['confirm'],
        request.POST['dob'],
    )
    if user[0]:
        request.session["user"] = {
            "id": user[1].id,
            "name": user[1].name
        }
        return redirect('/home')
    else:
        for error in user[1]:
            messages.add_message(request, messages.ERROR, error)
    return redirect('/')

def new_session(request):
    valid = User.userManager.login(
        request.POST['username'],
        request.POST['password']
    )
    if valid[0]:
        request.session["user"] = {
            "id": valid[1].id,
            "name": valid[1].name
        }
        return redirect('/home')
    else:
        for error in valid[1]:
            messages.add_message(request, messages.ERROR, error)
    return redirect('/')

def home(request):
    if 'user' not in request.session:
        return redirect('/')
    else:
        context = {
            'all_quotes': Quote.quoteManager.exclude(users=request.session['user']['id']),
            'faves': User.userManager.get(id=request.session['user']['id']).quotes.all(),
        }
        return render(request, "main_app/home.html", context)

def add(request):
    if 'user' not in request.session:
        return redirect('/')
    else:
        return render(request, 'main_app/add.html')



def process(request):

    if 'user' not in request.session:
        return redirect('/')
    if request.method == 'GET':
        return render(request, 'main_app/add.html')

    elif request.method == 'POST':
        quote = Quote.quoteManager.validate(
            request.POST['author'],
            request.POST['message'],
            request.session['user']['id']
            )
        if quote[0]:
            return redirect('/home')

        else:
            for error in quote[1]:
                messages.add_message(request, messages.ERROR, error)
    return redirect('/home/add')

def favorites(request, id):
    u = User.userManager.get(id=request.session['user']['id'])
    u.save()
    quote[1].users.add(u)
    quote[1].save()
    return redirect('/home')

def logout(request):
    request.session.clear()
    return redirect('/')

def uploader(request, id):
    if 'user' not in request.session:
        return redirect('/')

    else:
        quotes = Quote.quoteManager.filter(uploader_id=id)
        count = len(Quote.quoteManager.filter(uploader_id=id))
        context = {
            'quotes' : quotes,
            'count' : count,
        }
        return render(request, 'main_app/quotes.html', context)

def join(request, id):
    u = User.userManager.get(id=request.session['user']['id'])
    u.save()
    quote = Quote.quoteManager.get(id=id)
    quote.users.add(u)
    quote.save()
    return redirect('/home')

def remove(request, id):
    u = User.userManager.get(id=request.session['user']['id'])
    u.save()
    quote = Quote.quoteManager.get(id=id)
    u.quotes.remove(quote)
    u.save()
    return redirect('/home')

def dashboard(request):
    return redirect('/home')