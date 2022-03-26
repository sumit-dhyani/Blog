
from django.urls import path,include
from .views import Userregisterationview
urlpatterns = [
    path('register/' ,Userregisterationview.as_view(), name='register'),

]   