from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Allo. Ur at pollz indx")
def detail(request, question_id):
    return HttpResponse("Ur lookn at q %s"%question_id)
def results(request, question_id):
    return HttpResponse("Lookn rsults of q %s"%question_id)
def vote(request, question_id):
    return HttpResponse("Ur votn at q %s"%question_id)