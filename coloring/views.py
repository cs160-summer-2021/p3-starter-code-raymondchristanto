from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def new_interaction(request):
    return render(request, 'coloring/new_interaction.html')

def home(request):
    return render(request, 'coloring/home.html')

def home_dark(request):
    return render(request, 'coloring/home-dark.html')

def drawing(request):
    return render(request, 'coloring/drawing.html')