from django.contrib import admin
from api.models import Student

@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'roll', 'city', 'pass_by']
