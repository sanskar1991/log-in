from django.urls import path, include
from .views import home, register, signup

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    # path('signup/', signup, name='signup')
]
