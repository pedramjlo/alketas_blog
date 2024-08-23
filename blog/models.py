from django.db import models

from user_account.models import CustomUser




class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False)
    body = models.TextField(null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return f"{self.title} by {self.author}"

