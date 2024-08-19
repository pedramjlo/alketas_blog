from django.db import models
from user_account.models import CustomUser



class Avatar(models.Model):
    class AvatarSelect(models.CharField):
        WOMAN = 1, "static/woman.svg"
        MAN = 1, "static/man.svg"

    image = models.ImageField(upload_to='static/avatars/')





class Profile(models.Model):

    class RoleChoice(models.IntegerChoices):
        AUTHOR = 1, "Author"
        User = 2, "User"


    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    role = models.IntegerField(choices=RoleChoice.choices, default=RoleChoice.User)
    avatar = models.OneToOneField(Avatar, on_delete=models.CASCADE, null=True, blank=False)


    def __str__(self):
        return f"{self.user.username}'s profile"
