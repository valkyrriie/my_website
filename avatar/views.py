from django.shortcuts import render

def avatar_home(request):
    return render(request, 'main/avatar.html')
