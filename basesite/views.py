from django.shortcuts import render, HttpResponse
from .forms import Contact_form
from .models import Contact, Modeling, Art, Coading, Aprojects, Title, About, Work_des
from django.core.mail import send_mail
from selfsite import settings

# Create your views here.

def home(request):

    if request.method=='POST':
        form = Contact_form(request.POST)
        if form.is_valid():
            print("valid")
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            message =f"Hi {name},\n\nThank you for connecting.\n\nYour message,\n'{message}' has been recieved\n\nThis is automatically generated email, I'll revert back to you soon.\n\nThanks & Regards,\nHimanshu Kawale" 

            send_mail(f"{name} sent an email", message, settings.EMAIL_HOST_USER, [email])
            email = "none"
            return render(request, "basesite/index.html", {"models":models, "arts":arts, "codes":codes, "aprojects":aprojects, "title":title, "about":about, "work_des":work_des})
    
    models = Modeling.objects.all()
    arts = Art.objects.all()
    codes = Coading.objects.all()
    aprojects = Aprojects.objects.all()
    title = Title.objects.all()
    about = About.objects.all()
    work_des = Work_des.objects.all()

    return render (request, 'basesite/index.html', {"models":models, "arts":arts, "codes":codes, "aprojects":aprojects, "title":title, "about":about, "work_des":work_des})
