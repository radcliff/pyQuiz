# from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question, Answer

def index(request):
    return HttpResponse("<h1>Hello, world.</h1>")

def show(request, question_id):
    return HttpResponse('<h1>Hello, world.</h1>' + '<script>console.log(%(question_id)s)</script>' % locals())

def results(request, question_id):
    response = "This is the results of question %s."
    return HttpResponse(response % question_id)
