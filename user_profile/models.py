from django.db import models
from user_account.models import CustomUser



class Avatar(models.Model):
    class AvatarSelect(models.TextChoices):
        WOMAN = "static/avatars/lady-avatar.svg", "Woman"
        MAN = "static/avatars/man-avatar.svg", "Man"

    image = models.ImageField(upload_to='static/avatars/', default=AvatarSelect.WOMAN)

    
        




class Profile(models.Model):

    class RoleChoice(models.IntegerChoices):
        AUTHOR = 1, "Author"
        User = 2, "User"


    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    role = models.IntegerField(choices=RoleChoice.choices, default=RoleChoice.User)
    avatar = models.OneToOneField(Avatar, on_delete=models.CASCADE, null=True, blank=False)
    
    
    
    def change_avatar(self, new_avatar):
        self.avatar = new_avatar
        self.save()
        return self


    def change_role(self, new_role):
        self.role = new_role
        self.save()
        return self


    

    def __str__(self):
        return f"{self.user.username}'s profile"


    