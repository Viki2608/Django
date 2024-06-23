from django.urls import path

from . import views

urlpatterns = [
    path("cicd", views.cicd, name="cicd"),
    path("group_deploy", views.group_deploy, name="group_deploy"),
    path('process/', views.process_form, name='process_form'),
]
