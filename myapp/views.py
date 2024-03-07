from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    if request.method=='POST':
        message_name = request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']

        send_mail(
            'New Message!',
            f'Message from: {message_name}\nEmail: {message_email}\n\n{message}',
            message_email,
            [''],
        )

        return render(request, 'success.html', {'message_name': message_name})
    
    else:
        return render(request, 'home.html')

def success(request):
    return render(request, 'success.html')
