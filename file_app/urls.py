from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('', views.index, name='index'),
    path('faculty-list', views.faculty_list, name='faculty_list'),
    #path('<int:faculty_id>/files/', views.faculty_files, name='faculty_files'),

    path('faculty/archives-list', views.faculty_archives_list, name='faculty_archives_list'),
    path('staff/archives-list', views.staff_archives_list, name='staff_archives_list'),

    path('add/staff-documents', views.add_staff_document, name='add_staff_documents'),
    path('add/faculty-documents', views.add_faculty_document, name='add_faculty_documents'),
    path('department-list', views.department_list, name='department_list'),
    path('edit-department/<int:pk>/', views.edit_department, name='edit_department'),
    path('scan_documents', views.scan_document, name='scan_files'),
   # path('add_document', views.add_document, name='add_document'),
    path('staff-list', views.staff_list, name='staff_list'),
    path('edit_faculty/<int:pk>/edit', views.edit_faculty, name='edit_faculty'),
    path('delete_faculty/<int:pk>/', views.delete_faculty, name='delete_faculty'),
    path('faculty-details/<int:pk>/', views.faculty_details, name='faculty_details'),

]
