from django.shortcuts import redirect, render
from .models import Hiretuber
from django.contrib import messages

# Create your views here.


def hiretuber(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        city = request.POST['city']
        phone = request.POST['phone']
        state = request.POST['first_name']
        message = request.POST['message']
        user_id = request.POST['user_id']

        # TODO: dO all sanitization (means all the checking if all is in proper format or not)

        hiretuber = Hiretuber(
            first_name=first_name,last_name=last_name,email=email,tuber_id=tuber_id,tuber_name=tuber_name,city=city,phone=phone,state=state,message=message,user_id=user_id)

        hiretuber.save()
        messages.success(request,'Thanks for reaching out')
        return redirect('youtubers')