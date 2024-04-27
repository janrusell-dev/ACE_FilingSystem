from django import forms
from .models import Faculty, Department, Staff


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['first_name', 'middle_name', 'last_name', 'suffix_name', 'department', 'campus']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['code', 'name']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['first_name', 'middle_name', 'last_name',  'suffix_name', 'department', 'campus']




class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)



