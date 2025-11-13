from django.shortcuts import render

def home(request):
    return render(request, 'cafe/home.html')

def about(request):
    return render(request, 'cafe/about.html')

def study_rooms(request):
    return render(request, 'cafe/study_rooms.html')

def resources(request):
    return render(request, 'cafe/resources.html')

def contact(request):
    return render(request, 'cafe/contact.html')
