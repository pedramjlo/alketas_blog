from .models import CustomUser



def create_user(**kwargs):
    user = CustomUser.objects.create_user(
        username=kwargs.get('username'),
        first_name=kwargs.get('first_name'),
        last_name=kwargs.get('last_name'),
        email=kwargs.get('email'),
        password=kwargs.get('password'),
    )

    user.save()
    return user