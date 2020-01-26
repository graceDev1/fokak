from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import send_mail
from .models import Blog
# def contact(request):
#     subject = 'sending mail'
#     message = ' your mail has been sended successfully'
#     from_send = settings.EMAIL_HOST_USER
#     to_send = [settings.EMAIL_HOST_USER]
#     send_mail(subject, message, from_send, to_send, fail_silently=True)


def index(request):
    post = Blog.objects.all()

    context = {'posts': post}
    return render(request, 'index.html', context)