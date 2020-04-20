from django.contrib import admin

# Register your models here.
from .models import Task,Taskheading

admin.site.register(Task)
admin.site.register(Taskheading)