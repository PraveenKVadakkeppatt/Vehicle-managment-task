from django.contrib import admin
from .models import Desigination
# Register your models here.
class AdminDesigination(admin.ModelAdmin):
    list_display=['desigination']
admin.site.register(Desigination,AdminDesigination)
