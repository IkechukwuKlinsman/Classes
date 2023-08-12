from django.urls import path
from .views import homepage,homepage2

urlpatterns = [
    path('', homepage,name='home'),
    path('home/', homepage2,name='homepage'),

]