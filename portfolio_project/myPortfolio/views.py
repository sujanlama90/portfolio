from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

# Create your views here.

def home (request):
    return render(request,'myPortfolio/home.html')

def about(request):
    context = {
        "journey": Journey.objects.first(),
        "education": Education.objects.all(),
        "skill": Skill.objects.all(),
    }
    return render(request,'myPortfolio/about.html',context)

def skills(request):
    categories = SkillCategory.objects.prefetch_related("skills")
    return render(request,'myPortfolio/skills.html',{'categories':categories})

def project(request):
    searched = request.GET.get("searched")
    if searched:
        data=Project.objects.filter(title__contains=searched)
    else:
        data = Project.objects.all()
    return render(request,'myPortfolio/projects.html',{'data':data})

def contact(request):
    contact_info = MyContact.objects.first()
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message_text = request.POST['message']
        
        Contact.objects.create(name=name,email=email,subject=subject,message=message_text)
        
        email_subject = 'Thank you for connecting with us'
        # Email body message.
        email_body = render_to_string('myPortfolio/email_message.html', {
            'name': name,
            'subject': subject,
            'user_message': message_text,
        })
        # Sender's email address.
        from_email = settings.EMAIL_HOST_USER
        # List of recipient email addresses.
        recipient_list = [email]
        # Send the email to the recipient.
        send_mail(subject=email_subject, message=email_body, from_email=from_email, recipient_list=recipient_list, fail_silently=False)
        
        messages.success(request, f'Hi {name}, your message has been submitted.')
        return redirect('contact')
    return render(request,'myPortfolio/contact.html',{'contact':contact_info})