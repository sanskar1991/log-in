from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Users(models.Model):
    """
    User class to store data of users
    """
    email = models.EmailField(_("Email"), max_length=50, unique=True)
    username = models.CharField(_("Username"), max_length=15, unique=True)
    mob_number = models.IntegerField(_("Mobile Number"), unique=True)
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
    
    def __str__(self):
        """Convert object into string
        """
        return self.username
