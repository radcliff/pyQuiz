from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^quizzes/', include('quizzes.urls')),
    url(r'^admin/', include(admin.site.urls))
]
