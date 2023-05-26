from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'estate/index.html')

def about(request):
    return render(request, 'estate/about.html')

def services(request):
    return render(request, 'estate/services.html')

def contact(request):
    return render(request, 'estate/contact.html')