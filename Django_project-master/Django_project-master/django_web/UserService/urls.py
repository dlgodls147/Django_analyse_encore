from django.contrib import admin
from django.urls import path
from . import views

app_name = 'UserService'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.chart2, name='index1'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_check, name='login'),
    path('logout/', views.logout, name='logout'),
    path('visual1/', views.visual, name='visual'),
    path('result', views.result, name = 'result'),
    path('chartjson1/', views.chart1, name = 'chartjson1'),
    path('chartjson2/', views.chart3, name = 'chartjson2'),
    
    path('test/', views.htmldd,name='test'),
    path('test/', views.htmldd2,name='test'),
    ]