from .models import Post
from django.utils import timezone


def create_post(**kwargs):
    user = kwargs.get('author')
    if not user:
        raise ValueError("این نام کابری وجود ندارد!")
    
    if user.profile.role == 1:
            author=user, 
            title = kwargs.get('title'),
            body = kwargs.get('body'),
            created_at = kwargs.get('created_at', timezone.now()),

            if not title:
                raise ValueError("عنوان پست نباید خالی باشد")
            if not body: 
                raise ValueError("پست نمیتواند خالی باشد")
            

            new_post = Post.objects.create(
                author = user,
                title = title,
                body = body,
                created_at = created_at
            )

            return new_post
    else:
        raise PermissionError("شما اجازه ساخت و نشر پست ندارید!")
