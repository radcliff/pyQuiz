from django.conf.urls import url

from quizzes import views

urlpatterns = [
    # ex: /quizzes/
    url(r'^$', views.index, name='index'),
    # ex: /quizzes/5
    url(r'^(?P<question_id>[0-9]+)/$', views.show, name='detail'),
    # ex: /quizzes/5/results
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results')
]