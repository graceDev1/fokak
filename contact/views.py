from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import send_mail
from .models import Blog

def index(request):
    
    return render(request, 'index.html')

def post(request):
    post = Blog.objects.all()
    context = {'post': post}
    return render(request, 'post.html', context)

def about(request):
    list_about = [
        {
            'title': 'Qui nous sommes ?',
            'content': 'La FONDATION KALEHE KWETU, FOKAK en sigle, est une association sans '
                       'but lucratif de droit congolais  dont la vision est de voir les enfants, '
                       'les jeunes et les femmes vivre de façon autonome en exploitant les ressources et o'
                       'pportunités locales dans l’objectif de défendre et  promouvoir les intérȇts de la '
                       'population dans le domaine de santé, l’argiculture, l’élévage, la pȇche, l’éducation'
                       ' et la culture et sport. FOKAK asbl s’engage en terme de mission de créér  et '
                       'd’appuyer les initiatives locales de développemlent.'
        },
        {
            'title': 'Mission et Vision',
            'content': 'La FONDATION KALEHE KWETU, FOKAK en sigle, est une association sans but lucratif de droit congolais  dont la vision est de voir les enfants, les jeunes et les femmes vivre de façon autonome en exploitant les ressources et opportunités locales dans l’objectif de défendre et  promouvoir les intérêts de la population dans le domaine de santé, l’agriculture, l’élevage, la pêche, l’éducation et la culture et sport. FOKAK asbl s’engage en termes de mission de créer  et d’appuyer les initiatives locales de développement.'
        }

    ]
    context = {'about': list_about}
    return render(request, 'about.html', context)

def contact(request):
    if(request.method == 'POST'):
        form = ContactForm(request.POST)
        if (form.is_valid()):
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('body')
            send_mail(subject=name, message=content, from_email=email, recipient_list= [settings.EMAIL_HOST_USER])
            return redirect('/contact/')
    else:
        form = ContactForm
        return render(request, 'contact.html', {'form': form})
