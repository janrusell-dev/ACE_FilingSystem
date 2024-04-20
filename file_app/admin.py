from django.contrib import admin

# Register your models here
from .models import Department, Faculty, Staff, Campus, AddFacultyDocument, AddStaffDocument, AddStaffDocImage

admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Staff)
admin.site.register(Campus)
admin.site.register(AddFacultyDocument)
admin.site.register(AddStaffDocument)
admin.site.register(AddStaffDocImage)






