from django.contrib import admin

# Register your models here.
from .models import Task


# register my model to admin panel
admin.site.register(Task)