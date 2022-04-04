
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Userregisterationview
urlpatterns = [
    path('register/' ,Userregisterationview.as_view(), name='register'),

]   
urlpatterns = format_suffix_patterns(urlpatterns)