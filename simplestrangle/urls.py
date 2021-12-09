from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('create/', views.createnewposition, name='createnewpoisiont'),
    # ex: /polls/5/results/
    path('continue/', views.continueoldposition, name='continue'),
    # ex: /polls/5/vote/
    path('close/', views.closeallpositions, name='close'),
]