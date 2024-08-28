from .models import CustomUser


def create_user(*kwargs):
    user = CustomUser.objects.create_user(
        username=kwargs.get('username'),
        first_name= kwargs.get('firstt_name'),
        last_name=kwargs.get('last_name'),
        email=kwargs.get('email'),
    )
    user.set_password(kwargs.get('password'),)
    user.is_active = True
    user.save()
    return user