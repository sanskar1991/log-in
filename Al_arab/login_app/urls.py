from django.urls import path, include
from .views import home, register, verify_email

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('verify/', verify_email, name='verify'),
    # path('signup/', signup, name='signup')
]
