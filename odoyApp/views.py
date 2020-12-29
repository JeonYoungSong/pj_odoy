from django.shortcuts import render
from .models import *
# Create your views here.

def odoymain(request):
    return render(request, 'odoymain.html')


def secondPage(request):
    if(request.method == 'POST'):
        nickname = request.POST['nickname'] #String Type
        if request.POST['gender'] == 0:
            ngender = "female"
        else:
            ngender = "male"
        #ngender = request.POST['gender'] # String Type

        nbirth = request.POST['birth'] # DatetimeType
        nlife = request.POST['life']
        new_data = User_Info(name = nickname,gender = ngender,birth = nbirth,life = nlife)

        new_data.save()
        print(nickname + " " + ngender + " " + nbirth + " " + nlife)
    return render(request,'secondPage.html')
