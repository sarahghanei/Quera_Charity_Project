from accounts.models import User
from django.shortcuts import render


def about_us(request):
    users = User.objects.all()
    list_users = []
    for user in list(users):
        user = user.get_full_name()
        user += "          "
        list_users.append(user)

    context = {
        'users': list_users
    }
    return render(request, 'about_us.html', context)
