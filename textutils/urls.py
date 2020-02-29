from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('analyzeform/', views.analyze_form, name='analyze_form'),
    path('analyze', views.analyze, name='analyze'),  ## if the request is POST, don't use / after (analyze/)

]


