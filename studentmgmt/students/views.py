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
    
def add_student(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        courses = request.POST.get('courses')
        Student.objects.create(
            full_name=full_name,
            email=email,
            age=age,
            courses_id=courses
        )
        return render(request, 'add_student.html', 
                      {'message': 'Student added successfully!', 'courses': Course.objects.all()})
    return render(request, 'add_student.html', {'courses': Course.objects.all()})
    
def add_course(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Course.objects.create(name=name)
            return render(request, 'add_course.html', 
                          {'message': 'Course added successfully!'})
    return render(request, 'add_course.html', {})
    
def view_students(request):
    students = Student.objects.all()
    return render(request, 'view_students.html', {'students': students})

def view_courses(request):
    courses = Course.objects.all()
    return render(request, 'view_courses.html', {'courses': courses})

def edit_student(request, student_id):
    student = Student.objects.get(id=student_id)
    courses = Course.objects.all()
    if request.method == 'POST':
        student.full_name = request.POST.get('full_name')
        student.email = request.POST.get('email')
        student.age = request.POST.get('age')
        student.courses_id = request.POST.get('courses')
        student.save()
        return render(request, 'edit_student.html', 
                      {'student': student, 'courses': courses, 'message': 'Student updated successfully!'})
    return render(request, 'edit_student.html', {'student': student, 'courses': courses})

def edit_course(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        course.name = request.POST.get('name')
        course.save()
        return render(request, 'edit_course.html', 
                      {'course': course, 'message': 'Course updated successfully!'})
    return render(request, 'edit_course.html', {'course': course})

def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    students = Student.objects.all()
    return render(request, 'view_students.html', 
                  {'students': students, 'message': 'Student deleted successfully!'})
    
def delete_course(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    courses = Course.objects.all()
    return render(request, 'view_courses.html', 
                  {'courses': courses, 'message': 'Course deleted successfully!'})

