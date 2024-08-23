from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser, Group, Permission




class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

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

    



class CustomUser(AbstractUser):
    objects = CustomUserManager()





    def change_password(self, new_password):
        # save_password() method should be called not assgined!
        self.set_password(new_password)
        self.save(using=self._db)
        return self

    def __str__(self):
        return self.username


    def save(self, *args, **kwargs):
        from user_profile.models import Profile

        super().save(*args, **kwargs)

        if not hasattr(self, "profile"):
            Profile.objects.get_or_create(user=self)

