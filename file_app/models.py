from django.db import models
from django.utils import timezone


class Campus(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    code = models.CharField(max_length=15)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Define the Faculty model
class Faculty(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, default='')  # Added default value ''
    suffix_name = models.CharField(max_length=50, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        # Check if middle_name is not empty and has a value
        if self.middle_name:
            middle_initial = self.middle_name[0] + ". "  # Add period if middle_name is not empty
        else:
            middle_initial = ""  # No middle name, so no period
        full_name = f"{self.first_name} {middle_initial}{self.last_name}"
        if self.suffix_name:
            full_name += f", {self.suffix_name}"
        return full_name

class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, default='')  # Added default value ''
    suffix_name = models.CharField(max_length=50, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        # Check if middle_name is not empty and has a value
        if self.middle_name:
            middle_initial = self.middle_name[0] + ". "  # Add period if middle_name is not empty
        else:
            middle_initial = ""  # No middle name, so no period
        full_name = f"{self.first_name} {middle_initial}{self.last_name}"
        if self.suffix_name:
            full_name += f", {self.suffix_name}"
        return full_name




class AddFacultyDocument(models.Model):
    subject = models.TextField()
    file_upload = models.FileField(upload_to='files/', null=True)
    date_added = models.DateField(default=timezone.now)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.department} - {self.campus} - {self.date_added}"

class AddStaffDocument(models.Model):
    subject = models.TextField()
    file_upload = models.FileField(upload_to='files/', null=True)
    date_added = models.DateField(default=timezone.now)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.department} - {self.campus} - {self.date_added}"











