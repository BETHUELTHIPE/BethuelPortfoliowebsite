from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from .forms import ContactForm
from .models import Contact  # Import your Contact model

# Home view
def home(request):
    return render(request, "home.html")

# About view
def about(request):
    return render(request, "about.html")

# Projects view
def projects(request):
    projects_show = [
        {
            'title': 'cloud-computing-project',
            'path': 'images/serverless_DESIGN_project.png',
            'link': 'https://github.com/BETHUELTHIPE/cloud-computing-predict'
        },
        {
            'title': 'moving-big-data-project-airflow',
            'path': 'images/Streaming data.png',
            'link': 'https://github.com/BETHUELTHIPE/moving-big-data-predict-airflow'
        },
        {
            'title': 'data-migration-on-premise-to-aws',
            'path': 'images/Storingbigdata.png',
            'link': 'https://github.com/BETHUELTHIPE/data-migration-on-premise-to-aws'
        },
        {
            'title': 'Integrated-project',
            'path': 'images/insurance_data_ETL.png',
            'link': 'https://github.com/BETHUELTHIPE/Integrated-project'
        },
        {
            'title': 'processing-big-data-predict',
            'path': 'images/end-to-end-pipeline.jpg',
            'link': 'https://github.com/BETHUELTHIPE/processing-big-data-predict'
        },
        {
            'title': 'Store-BIG-DATA-PROJECT01',
            'path': 'images/end-to-end-pipeline.jpg',
            'link': 'https://github.com/BETHUELTHIPE/Store-BIG-DATA-PROJECT01'
        },
    ]
    return render(request, "projects.html", {"projects_show": projects_show})

# Experience view
def experience(request):
    experience = [
        {"company": "EXPLOREAI Cape Town South Africa", "position": "Data Engineer Intern"},
        {"company": "Department of Higher Education and Training", "position": "Mathematics and Physics Lecturer"},
        {"company": "Umalusi Quality Council", "position": "Evaluator/Subject Specialist/Team Leader"},
        {"company": "Audrin Developers", "position": "Web Applications Developer"},
    ]
    return render(request, "experience.html", {"experience": experience})

# Certificate view
def certificate(request):
    return render(request, "certificate.html")

# Contact view
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('success')  # Redirect to a success page
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

# Resume download view
def resume(request):
    resume_path = "myapp/resume.pdf"
    resume_path = staticfiles_storage.path(resume_path)
    
    if staticfiles_storage.exists(resume_path):
        with open(resume_path, "rb") as resume_file:
            response = HttpResponse(resume_file.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
            return response
    else:
        return HttpResponse("Resume not found", status=404)

# Success view
def success_view(request):
    return render(request, 'success.html')
