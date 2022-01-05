from django.shortcuts import redirect, render
from .models import Project
from django.conf import settings
from django.core.mail import message, send_mail
# Create your views here.


def home(request):
    projects = Project.objects.all()
    
    return render(request, 'portfolio/index.html', {'projects':projects})

def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        msg = f'Message from {first_name} {last_name}\n'
        msg += f'Email address: {email}\n'
        msg += f'Message: "{message}"\n'

        # send email
        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS],
        )

        # return render(request, 'portfolio/index.html', {'projects':projects, 'success':first_name})
        return render(request, 'portfolio/success.html', {'success':first_name})

