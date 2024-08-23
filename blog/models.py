from django.db import models
from django.utils import timezone

from user_account.models import CustomUser



class Category(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self) -> str:
        return self.name





class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False)
    body = models.TextField(null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    last_edited = models.DateTimeField(null=True)
    

    def update_last_edited(self, new_date):
        self.last_edited = timezone.now()
        self.save(using=self._db)
        return self


    def edit_article(self, new_edit):
        self.body = new_edit
        self.save(using=self._db)
        self.update_last_edited()
        return self



    def __str__(self):
        return f"{self.title} by {self.author}"
    



    