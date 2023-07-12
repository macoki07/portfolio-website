from django.urls import path,re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("resume", views.resume, name="resume"),
    path("projects", views.projects, name="projects"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("edit_profile", views.edit_profile, name="edit_profile"),
    path("edit_section/<str:title>", views.edit_section, name="edit_section"),
    path("edit_project/<str:title>", views.edit_project, name="edit_project"),
    path("add_section", views.add_section, name="add_section"),
    path("add_project", views.add_project, name="add_project")
]
