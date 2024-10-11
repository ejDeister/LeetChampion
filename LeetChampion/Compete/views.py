from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from . import forms

# Define a default view (header, navbar, footer etc.) that content will be injected into
def index(request):
    return render(request, 'index.html')

# Define a home view
def home(request):
    return render(request, 'home.html')

# Define a dashboard view
def dashboard(request):
    return render(request, 'dashboard.html')

# Define a view to either conenct a user to a lobby or host their own
def lobby(request):
    return render(request, 'lobby.html')

# Define a view to get an LC problem
def get_poblem(request):
    return render(request, 'get-problem.html')

# Define a view to run a solution to an LC problem
def run(request):
    return render(request, 'run-solution.html')

# Define a view to submit a solution to an LC problem
def submit(request):
    return render(request, 'submit-solution.html')

# Define a view to display results of a battle
def results(request):
    return render(request, 'results.html')