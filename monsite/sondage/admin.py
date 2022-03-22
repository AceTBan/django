from django.contrib import admin

# Register your models here.

from .models import Citizen, Question, Choice

admin.site.register(Question)
admin.site.register(Choice)

admin.site.register(Citizen)