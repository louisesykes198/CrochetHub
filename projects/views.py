from django.shortcuts import render
from django.http import HttpResponse

# Home page view
def home(request):
    return HttpResponse("Welcome to CrochetHub - Your Crochet Project Hub!")

# Add other views for your app if needed, for example, a view for viewing projects:

# Project listing view (for showing all crochet projects)
def project_list(request):
    # Assuming you have a model named Project, you would fetch projects here.
    # For now, let's just return a simple message.
    return HttpResponse("Here is a list of crochet projects")

# A view for a specific project detail page (this could be a placeholder)
def project_detail(request, project_id):
    # In a real scenario, you would fetch a project based on `project_id`
    return HttpResponse(f"Details of project {project_id}")