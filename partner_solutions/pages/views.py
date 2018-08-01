from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {"home_page": "active"} # new info here
    return render(request, 'pages/index.html', context)
def partner(request):
    context = {"partner_page": "active"} # new info here
    return render(request, 'pages/partner.html', context)
def study_center(request):
    context = {"studycenter_page": "active"} # new info here
    return render(request, 'pages/study_center.html', context)
def chatbot(request):
    context = {"chatbot_page": "active"} # new info here
    return render(request, 'pages/chatbot.html', context)
def about(request):
    context = {"about_page": "active"} # new info here
    return render(request, 'pages/about.html', context)
def contact(request):
    context = {"contact_page": "active"} # new info here
    return render(request, 'pages/contact.html', context)
