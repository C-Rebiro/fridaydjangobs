from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def category(request):
    return render(request, 'category.html')

def work(request):
    return render(request, 'work.html')

# Create your views here.
