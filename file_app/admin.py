from django.contrib import admin

# Register your models here
from .models import Department, Faculty, Staff, Campus, StaffArchivesFile, StaffArchives, FacultyArchivesFile, FacultyArchives

admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Staff)
admin.site.register(Campus)
admin.site.register(StaffArchives)
admin.site.register(StaffArchivesFile)
admin.site.register(FacultyArchives)
admin.site.register(FacultyArchivesFile)








