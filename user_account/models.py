from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission



class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, blank=False, null=False, unique=True)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    password = models.CharField(max_length=100, unique=True, blank=False, null=False)
    has_selected_avatar = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']



    def __str__(self):
        return self.username


    def save(self, *args, **kwargs):
        from user_profile.models import Profile

        super().save(*args, **kwargs)

        if not hasattr(self, "profile"):
            Profile.objects.get_or_create(user=self)

