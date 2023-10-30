from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from actstream import action

def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        notify = request.POST.get('notify') == 'on'
        
        if notify:
            send_mail(
                'Test notification',
                'This is a test notification.',
                'hi@gmail.com', # replace with email entered in settings.py/EMAIL_HOST_USER
                [email],
                fail_silently=False,
            )

            action.send(request.user, verb='received email notification', target=email)
            
            return HttpResponseRedirect('/success/')
    return render(request, 'polls/index.html')

def success(request):
    return render(request, 'polls/success.html')