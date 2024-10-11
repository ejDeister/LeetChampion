from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from . import forms

# Define a default view
def index(request):
    return render(request, 'index.html')

# Define a default view
def home(request):
    return render(request, 'home.html')

# Define a default view
def dashboard(request):
    return render(request, 'dashboard.html')

# Define a default view
def lobby(request):
    return render(request, 'lobby.html')

# Define a default view
def run(request):
    return render(request, 'run-solution.html')

# Define a default view
def submit(request):
    return render(request, 'submit-solution.html')

# Define a default view
def results(request):
    return render(request, 'results.html')