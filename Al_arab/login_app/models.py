from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class UserRegister(models.Model):
    """
    User class to store data of users
    """
    email = models.EmailField(
        _("Email"), 
        max_length=50, 
        unique=True, 
        help_text="Verification email will be sent to this email."
        )
    username = models.CharField(
        _("Username"), 
        max_length=15, 
        unique=True,
        help_text="This will be used to identify you profile."
        )
    mob_number = models.IntegerField(
        _("Mobile Number"), 
        unique=True,
        help_text="Verification code will be sent on this number."
        )
    password = models.CharField(
        _("Password"), 
        max_length=25,
        help_text="<ul> \
            <li>Your password can 't be too similar to your other personal information.</li> \
            <li>Your password must contain at least 8 characters.</li> \
            <li>Your password can 't be a commonly used password.</li> \
            <li>Your password can 't be entirely numeric.</li> \
            </ul>"
        )
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
    
    def __str__(self):
        """Convert object into string
        """
        return self.username
