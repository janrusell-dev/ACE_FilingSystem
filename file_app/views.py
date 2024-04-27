from .models import Department, Faculty, Campus, Staff, StaffArchives, StaffArchivesFile, FacultyArchives, FacultyArchivesFile
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import FacultyForm, DepartmentForm, StaffForm, LoginForm
from django.db.models import Count
from django.contrib.auth import authenticate, login, logout


@login_required
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to the index page after successful login
            else:
                return redirect('login')  # Redirect back to the login page with error message
    else:
        form = LoginForm()
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def index(request):
    faculties = Faculty.objects.all()
    faculty_count = faculties.count()

    departments = Department.objects.all()
    department_count = departments.count()

    staffs = Staff.objects.all()
    staff_count = staffs.count()

    faculty_documents_count = FacultyArchives.objects.count()
    staff_documents_count = StaffArchives.objects.count()

    total_files_count = (
        FacultyArchives.objects.count()
        + StaffArchives.objects.count()
    )
    recent_faculty_documents = FacultyArchives.objects.order_by('-date_added')[:10]
    recent_staff_documents = StaffArchives.objects.order_by('-date_added')[:10]

    context = {'faculty_count': faculty_count,
               'department_count': department_count,
               'staff_count': staff_count,
               'total_files_count': total_files_count,
                'recent_faculty_documents': recent_faculty_documents,
             'recent_staff_documents': recent_staff_documents,
              'faculty_documents_count': faculty_documents_count,
              'staff_documents_count': staff_documents_count}

    return render(request, 'index.html', context)


@login_required
def faculty_list(request):
    campuses = Campus.objects.all()
    faculties = Faculty.objects.all()
    departments = Department.objects.all()

    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            faculty = form.save()
            return redirect(request.path)
    else:
        form = FacultyForm()

    context = {
        'faculties': faculties,
        'departments': departments,
        'form': form,
        'campuses': campuses
    }

    return render(request, 'faculty_list.html', context)

@login_required
def update_faculty(request, id):
    faculty = get_object_or_404(Faculty, pk=id)
    if request.method == "POST":
        form = FacultyForm(request.POST, instance=faculty)
        if form.is_valid():
            form.save()
            return redirect('faculty_list')
    else:
        form = FacultyForm(instance=faculty)
    return render(request, 'update_faculty.html', {'form': form, 'faculty': faculty})

@login_required
def delete_faculty(request, id):
    faculty = get_object_or_404(Faculty, id=id)
    if request.method == 'POST':
        faculty.delete()
        return redirect('faculty_list')


    return redirect('faculty_list')




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


@login_required
def update_department(request, id):
    department = get_object_or_404(Department, pk=id)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'update_department.html', {'form': form, 'department': department})

@login_required
def delete_department(request, id):
    department = get_object_or_404(Department, id=id)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')


    return redirect('department_list')


@login_required
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
def update_staff(request, id):
    staff = get_object_or_404(Staff, pk=id)
    if request.method == "POST":
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm(instance=staff)
    return render(request, 'update_staff.html', {'form': form, 'staff': staff})


@login_required
def delete_staff(request, id):
    staff = get_object_or_404(Staff, id=id)
    if request.method == 'POST':
        staff.delete()
        return redirect('staff_list')


    return redirect('staff_list')


@login_required
def add_staff_document(request):
    recent_document = StaffArchives.objects.order_by('-date_added')[:10]
    campuses = Campus.objects.all()
    staffs = Staff.objects.all()
    departments = Department.objects.all()
    context = {'campuses': campuses,
               'staffs': staffs,
               'departments': departments}

    if request.method == 'POST':
        subject = request.POST['subject']
        department_id = request.POST['department']
        campus_id = request.POST['campus']
        staff_id = request.POST['staff']
        files = request.FILES.getlist('files')

        staff_archives = StaffArchives.objects.create(
            subject=subject,
            department_id=department_id,
            campus_id=campus_id,
            staff_id=staff_id
        )

        for file in files:
            StaffArchivesFile.objects.create(archives=staff_archives, file=file)

        return redirect(request.path)



    context = {
        'departments': departments,
        'campuses': campuses,
        'staffs': staffs,
        'recent_document': recent_document
    }

    return render(request, 'add_staff_document.html', context)

@login_required
def add_faculty_document(request):
    recent_document = FacultyArchives.objects.order_by('-date_added')[:10]
    campuses = Campus.objects.all()
    faculties = Faculty.objects.all()
    departments = Department.objects.all()

    context = {'campuses': campuses,
               'faculties': faculties,
               'departments': departments,
               'recent_document': recent_document}

    if request.method == 'POST':
        subject = request.POST['subject']
        department_id = request.POST['department']
        campus_id = request.POST['campus']
        faculty_id = request.POST['faculty']
        files = request.FILES.getlist('files')

        faculty_archives = FacultyArchives.objects.create(
            subject=subject,
            department_id=department_id,
            campus_id=campus_id,
            faculty_id=faculty_id
        )

        for file in files:
            FacultyArchivesFile.objects.create(archives=faculty_archives, file=file)

        return redirect(request.path)


    return render(request, 'add_faculty_document.html', context)

@login_required
def staff_archives_list(request):
    staff_docs  =  StaffArchives.objects.prefetch_related('files')
    departments = Department.objects.all()
    campuses = Campus.objects.all()
    context = {
        'departments': departments,
        'campuses': campuses,
        'staff_docs': staff_docs
    }

    return render(request, 'staff_archives_list.html', context)

@login_required
def faculty_archives_list(request):
    faculty_docs = FacultyArchives.objects.prefetch_related('files')
    departments = Department.objects.all()
    campuses = Campus.objects.all()
    context = {'departments': departments,
                'campuses': campuses,
                'faculty_docs': faculty_docs
               }
    return render(request, 'faculty_archives_list.html', context)

