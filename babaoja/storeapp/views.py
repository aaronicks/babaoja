from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def user_profile(request):
    return render(request, 'user_profile.html', {})
