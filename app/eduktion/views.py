from django.shortcuts import render
from django.core.mail import send_mail


def home(request):

    return render(request, 'eduktion/Home.html', locals())

def about(request):

    return render(request, 'eduktion/About.html', locals())

def contact(request):

    if request.method=='POST':
        email = request.POST.get('email')
        name = request.POST.get('name');
        subject = request.POST.get('subject');
        message = request.POST.get('message');

        print("{} {} ".format(email, message))

        send_mail(
            name,
            message,
            email,
            ['gibrillongmene@gmail.com'],
            fail_silently=False
        )

    return render(request, 'eduktion/Contact.html', locals())

def service(request):
    
    return render(request, 'eduktion/Service.html', locals())