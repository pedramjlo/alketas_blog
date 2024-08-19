from django.db import models
from user_account.models import CustomUser




class Profile(models.Model):

    class RoleChoice(models.IntegerChoices):
        AUTHOR = 1, "Author"
        User = 2, "User"


    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    role = models.IntegerField(choices=RoleChoice.choices, default=RoleChoice.User)
