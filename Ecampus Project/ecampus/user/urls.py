from django import views
from django.contrib import admin
from django.urls import path,include
from user import views
from .views import FacultySignupView, ParentSignupView, StudentSignupView, MultiLoginView

app_name = 'ecampus_urls'

urlpatterns = [
    path("index/",views.index),
    path("facultysignup/",FacultySignupView.as_view(),name="facultysignup"),
    path("studentsignup/",StudentSignupView.as_view(),name="studentsignup"),
    path("parentsignup/",ParentSignupView.as_view(),name="parentsignup"),
    path("multiuserview/",MultiLoginView.as_view(),name="multiuserview"),
    path('sendmail/',views.sendmail,name='send_mail'),

]