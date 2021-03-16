from django.contrib import admin
from .models import UserRegister

# Register your models here.
@admin.register(UserRegister)
class UsersAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'email',
        'username',
        'mob_number'
    ]
    Ordering = ['id']
