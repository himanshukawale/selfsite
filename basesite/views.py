from django.shortcuts import render, HttpResponse
from .forms import Contact_form
from .models import Contact, Modeling, Art, Coading, Aprojects, Title, About, Work_des
from selfsite import settings

def home(request):

    models = Modeling.objects.all()
    arts = Art.objects.all()
    codes = Coading.objects.all()
    aprojects = Aprojects.objects.all()
    title = Title.objects.all()
    about = About.objects.all()
    work_des = Work_des.objects.all()

    if request.method=='POST':
        form = Contact_form(request.POST)
        if form.is_valid():
            print("valid")
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            contact = Contact(name=name, email=email, message=message)
            contact.save()
            return render(request, "basesite/index.html", {"models":models, "arts":arts, "codes":codes, "aprojects":aprojects, "title":title, "about":about, "work_des":work_des})
    
    return render (request, 'basesite/index.html', {"models":models, "arts":arts, "codes":codes, "aprojects":aprojects, "title":title, "about":about, "work_des":work_des})
