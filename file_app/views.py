from .models import Department, Faculty, Campus, Staff, AddFacultyDocument, AddStaffDocument
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import FacultyForm, DepartmentForm, StaffForm,AddFacultyDocumentForm, AddStaffDocumentForm
from django.db.models import Count
from django.http import JsonResponse, HttpResponse
from django.contrib import messages

def scan_document(request):
    return render(request, 'scan.html')

@login_required
def login(request):
    return render(request, 'login.html')

@login_required
def index(request):
    faculties = Faculty.objects.all()
    faculty_count = faculties.count()
    departments = Department.objects.all()
    department_count = departments.count()
    staffs = Staff.objects.all()
    staff_count = staffs.count()
    context = {'faculty_count': faculty_count,
               'department_count': department_count,
               'staff_count': staff_count}

    return render(request, 'index.html', context)


@login_required
def faculty_list(request):
    campuses = Campus.objects.all()
    faculties = Faculty.objects.all()
    departments = Department.objects.all()

    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            faculty = form.save()  # Save the form to create a Faculty instance
            messages.success(request, 'Faculty added successfully.')
            return redirect('faculty_list')  # Redirect back to the faculty list page
    else:
        form = FacultyForm()

    context = {
        'faculties': faculties,
        'departments': departments,
        'form': form,
        'campuses': campuses
    }

    return render(request, 'faculty_list.html', context)

def edit_faculty(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    if request.method == 'POST':
        form = FacultyForm(request.POST, instance=faculty)
        if form.is_valid():
            form.save()
            return redirect('faculty_list')
    else:
        form = FacultyForm(instance=faculty)
    context = {'form': form,
               'faculty': faculty}
    return render(request, 'edit_faculty.html', context)

def faculty_details(request, pk):
    try:
        faculty = Faculty.objects.get(pk=pk)
        data = {
            'success': True,
            'faculty': {
                'id': faculty.id,
                'first_name': faculty.first_name,
                # Add other faculty details here
            }
        }
        return JsonResponse(data)
    except Faculty.DoesNotExist:
        data = {'success': False}
        return JsonResponse(data)


def delete_faculty(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    if request.method == 'POST':
        faculty.delete()
        return redirect('faculty_list')
    context = {'faculty': faculty}
    return render(request, 'delete_faculty.html', context)



@login_required
def department_list(request):
    departments = Department.objects.annotate(faculty_count=Count('faculty'), staff_count=Count('staff'))

    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)  # Redirect to the same URL
    else:
        form = DepartmentForm()

    faculties = Faculty.objects.all()
    faculty_count = faculties.count()

    context = {
        'departments': departments,
        'faculties': faculties,
        'faculty_count': faculty_count,
        'form': form,
    }

    return render(request, 'department_list.html', context)

def staff_list(request):
    staffs = Staff.objects.all()
    campuses = Campus.objects.all()
    departments = Department.objects.all()

    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            staff = form.save()  # Save the form to create a Faculty instance
            return redirect('staff_list')  # Redirect with the faculty ID
    else:
        form = StaffForm()

    context = {'staffs': staffs,
               'campuses': campuses,
               'departments': departments,
               'form': form
               }
    return render(request, 'staff_list.html', context)




@login_required
def edit_department(request, pk):
    department = get_object_or_404(Department, pk=pk)

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')  # Redirect to department list page after editing
    else:
        form = DepartmentForm(instance=department)

    return render(request, 'edit_department.html', {'form': form})




@login_required
def faculty_archives_list(request):
    faculty_docs = AddFacultyDocument.objects.all()
    departments = Department.objects.all()
    documents = AddFacultyDocument.objects.all()
    campuses = Campus.objects.all()
    context = {'departments': departments,
                'campuses': campuses,
                'documents': documents,
                'faculty_docs': faculty_docs
               }
    return render(request, 'faculty_archives_list.html', context)


def add_staff_document(request):
    departments = Department.objects.all()
    campuses = Campus.objects.all()
    staffs = Staff.objects.all()

    if request.method == 'POST':
        form = AddStaffDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form without committing to access the file field as a list
            instance = form.save(commit=False)
            files = request.FILES.getlist('file_upload')  # Get multiple files
            for f in files:
                # Assign each file to the instance's file_upload field
                instance.file_upload = f
                instance.save()
            # Redirect or display a success message
            return redirect('staff_archives_list')
    else:
        form = AddStaffDocumentForm()

    context = {
        'form': form,
        'departments': departments,
        'campuses': campuses,
        'staffs': staffs,
    }

    return render(request, 'add_staff_document.html', context)


def add_faculty_document(request):
    if request.method == 'POST':
        form = AddFacultyDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('faculty_archives_list')
    else:
        form = AddFacultyDocumentForm()

    departments = Department.objects.all()
    campuses = Campus.objects.all()
    faculties = Faculty.objects.all()


    context = {'departments': departments,
               'campuses': campuses,
               'faculties': faculties,
               'form': form}

    return render(request, 'add_faculty_document.html', context)

@login_required
def staff_archives_list(request):
    staff_docs = AddStaffDocument.objects.all()
    departments = Department.objects.all()
    campuses = Campus.objects.all()
    context = {
        'departments': departments,
        'campuses': campuses,
        'staff_docs': staff_docs
    }

    return render(request, 'staff_archives_list.html', context)


