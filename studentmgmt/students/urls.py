from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_course/', views.add_course, name='add_course'),
    path('view_students/', views.view_students, name='view_students'),
    path('view_courses/', views.view_courses, name='view_courses'),
    path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('edit_course/<int:course_id>/', views.edit_course, name='edit_course'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
]
