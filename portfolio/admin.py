from django.contrib import admin

from .models import Profile, Project, Section, User

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Section)
admin.site.register(Project)