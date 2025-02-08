from django.shortcuts import render
from .forms import ContactForm
from .models import Project, About

def home(request):
    projects = Project.objects.all()
    about = About.objects.first()  # Assuming you only have one About entry

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Handle form submission here, e.g., sending an email
            return render(request, 'portfolio/contact_success.html')  # Success page
    else:
        form = ContactForm()

    return render(request, 'portfolio/home.html', {
        'projects': projects,
        'about': about,
        'form': form
    })


