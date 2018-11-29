import csv
import datetime
from django.contrib import admin
from django.http import HttpResponse
from .models import Stream


@admin.register(Stream)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
