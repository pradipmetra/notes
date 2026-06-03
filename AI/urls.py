from django.urls import include, path
from .views import *

urlpatterns = [
    path('',fpage),
    path('login',user_login,name='loginn'),
    path('re',reg,name='registration'),
    path('logout',logout,name='logout'),
    path('dash',dashboard,name='dashboard'),
    path('contact',contact,name='contact'),
    path('about',about,name='about'),
    path('hello',ai_chat,name='AI'),
]