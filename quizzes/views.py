from django.shortcuts import render
from quizzes.models import Question, Answer

def index(request):
    questions = Question.objects.all()
    context = { 'questions': questions }
    return render(request, 'quizzes/index.html', context)
