from django import forms
from django.forms import ModelForm
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Max
from django.db import models
import markdown
import os
from django.contrib.auth import authenticate, login, logout
from portfolio.models import Profile, Project, Section
from django.core.paginator import Paginator
from portfolio.forms import AddProjectForm, EditProfileForm, EditProjectForm, EditSectionForm, AddSectionForm

# markdown to html
def section_convert_md_to_html(content):
    md = markdown.Markdown()
    if content == None:
        return "No Content"
    else:
        return md.convert(content)


def detail_convert_md_to_html(content):
    md = markdown.Markdown()
    if content == None:
        return "No Content"
    else:
        return md.convert(content)

def get_name():
    return Profile.objects.get(pk=1).name

def index(request):
    profile_data = Profile.objects.get(pk=1)
    
    return render(request, "portfolio/about.html", {"profile": profile_data,
    "name": get_name()})


def resume(request):
    all_sections = Section.objects.all().order_by("priority")
    sections = {}
    for section in all_sections:
        sections[section.title] = section_convert_md_to_html(section.description)

    return render(request, "portfolio/resume.html", {"sections": sections,
    "name": get_name()})


def projects(request):
    all_projects = Project.objects.all().order_by("priority")
    paginator = Paginator(all_projects, 1)
    page_num = request.GET.get("page")
    page_projects = paginator.get_page(page_num)

    project_details = {}
    for detail in all_projects:
        project_details[detail.title] = detail_convert_md_to_html(detail.details)

    return render(
        request,
        "portfolio/projects.html",
        {"page_projects": page_projects, "details": project_details,
    "name": get_name()},
    )


def edit_profile(request):
    try:
        profile = Profile.objects.get(pk=1)
    except:
        return HttpResponse(f"PROFILE NOT FOUND")
    if request.user.is_authenticated:
        form = EditProfileForm(
            request.POST or None, request.FILES or None, instance=profile
        )

        existing_picture = profile.picture
        if form.is_valid():
            if profile.picture != existing_picture:
                os.remove(existing_picture.path)
            form.save()
            return redirect("index")

        return render(request, "portfolio/edit_profile.html", {"form": form,
        "name": get_name()})
    else:
        return render(request, "portfolio/edit_profile.html", {
        "name": get_name()})


def edit_section(request, title):
    try:
        section = Section.objects.get(title=title)
    except:
        return HttpResponse(f"{title.upper()} NOT FOUND")
    if request.user.is_authenticated:
        form = EditSectionForm(request.POST or None, instance=section)
        old_priority = section.priority

        if form.is_valid():
            action = request.POST.get('action')
            if action == 'Update':
                new_priority = form.cleaned_data["priority"]
                if new_priority != old_priority:
                    # Find the section with the new priority
                    try:
                        existing_section = Section.objects.get(priority=new_priority)

                    except Section.DoesNotExist:
                        existing_section = None

                    if existing_section:
                        # Swap priorities with the existing section
                        existing_section.priority = old_priority
                        existing_section.save()

                    section.priority = new_priority
                    section.save()
                # Update the priority of the current section
                
                form.save()
                return redirect("resume")
                
            elif action == 'Delete':
                # Get the priority of the section being deleted
                deleted_priority = section.priority
                section.delete()
                # Update the priorities of the remaining sections
                Section.objects.filter(priority__gt=deleted_priority).update(priority=models.F('priority') - 1)
                return redirect("resume")


        return render(request, "portfolio/edit_section.html", {"form": form,
        "name": get_name()})
    else:
        return render(request, "portfolio/edit_section.html", {
        "name": get_name()})
def add_section(request):
    if request.user.is_authenticated:
        form = AddSectionForm(
            request.POST
        )

        if form.is_valid():
            section = form.save(commit=False)
            max_priority = Section.objects.aggregate(Max('priority'))['priority__max']
            section.priority = max_priority + 1 if max_priority is not None else 1
            section.save()
            return redirect("resume")

        return render(request, "portfolio/add_section.html", {"form": form,
        "name": get_name()})
    else:
        return render(request, "portfolio/add_section.html", {
        "name": get_name()})

def edit_project(request, title):
    try:
        project = Project.objects.get(title=title)
    except:
        return HttpResponse(f"{title.upper()} NOT FOUND")
    if request.user.is_authenticated:
        form = EditProjectForm(request.POST or None,request.FILES or None, instance=project)
        old_priority = project.priority

        if form.is_valid():
            action = request.POST.get('action')
            if action == 'Update':
                new_priority = form.cleaned_data["priority"]
                if new_priority != old_priority:
                    # Find the section with the new priority
                    try:
                        existing_project = Project.objects.get(priority=new_priority)

                    except Section.DoesNotExist:
                        existing_project = None

                    if existing_project:
                        # Swap priorities with the existing section
                        existing_project.priority = old_priority
                        existing_project.save()

                    project.priority = new_priority
                    project.save()
                # Update the priority of the current section
                
                form.save()
                return redirect("projects")
                
            elif action == 'Delete':
                # Get the priority of the section being deleted
                deleted_priority = project.priority
                project.delete()
                # Update the priorities of the remaining sections
                Project.objects.filter(priority__gt=deleted_priority).update(priority=models.F('priority') - 1)
                return redirect("projects")


        return render(request, "portfolio/edit_project.html", {"form": form,
        "name": get_name()})
    else:
        return render(request, "portfolio/edit_project.html", {
        "name": get_name()})
    
def add_project(request):
    if request.user.is_authenticated:
        form = AddProjectForm(
            request.POST, request.FILES
        )

        if form.is_valid():
            project = form.save(commit=False)
            max_priority = Project.objects.aggregate(Max('priority'))['priority__max']
            project.priority = max_priority + 1 if max_priority is not None else 1
            project.save()
            return redirect("projects")

        return render(request, "portfolio/add_project.html", {"form": form,
        "name": get_name()})
    
    else:
        return render(request, "portfolio/add_project.html", {
        "name": get_name()})

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "portfolio/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "portfolio/login.html",{
    "name": get_name()})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
