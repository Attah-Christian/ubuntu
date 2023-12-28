from django.shortcuts import render, redirect
from .models import UserFormGrabber
# Create your views here.



def index(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        country = request.POST['country']
        message = request.POST['message']


        UserFormSM = UserFormGrabber(firstname=firstname, lastname=lastname, email=email, phone=phone, country=country, message=message,)
        UserFormSM.save()


        return redirect('success')
    else:
        return render(request, 'index.html')


def success(request):
    return render(request, 'success.html')
