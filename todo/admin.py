from django.contrib import admin

# Register your models here.

from .models import ToDo, SingleInstruction

admin.site.register(ToDo)
admin.site.register(SingleInstruction)