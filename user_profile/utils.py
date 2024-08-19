# check for valid images
from .models import Avatar


def check_image(image, request):
    queryset = Avatar.objects.all()
    user = request.user 
    if image in queryset:
        if not user.has_selected_avatar:
            user.avatar = image
            user.has_selected_avatar = True
            user.save()
            return user
    else:
        return ValueError("این عکس وجود ندارد!")
