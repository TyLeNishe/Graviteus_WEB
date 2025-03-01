from django.urls import path
from .views import home
from .views import SignUp
from .views import LogIn

urlpatterns = [
    path('', home, name='home'),
    path('SignUp/', SignUp, name='SignUp'),
    path('LogIn/', LogIn, name='LogIn'),
]
