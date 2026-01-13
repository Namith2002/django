from django.shortcuts import render
from .models import Student, Course

# Create your views here.
def dashboard(request):
    
    students_count = Student.objects.count()
    courses_count = Course.objects.count()
    return render(request, 'dashboard.html', {
        'students_count': students_count,
        'courses_count': courses_count
    })