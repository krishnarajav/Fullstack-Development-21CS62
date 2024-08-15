from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import RegistrationForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courselist.html', {'courses':courses})

def course_detail(request, c_id):
    course = get_object_or_404(Course, c_id=c_id)
    students = course.enrollment.all()
    return render(request, 'coursedetail.html', {'course': course, 'students': students})   

def registration(request, c_id):
    course = get_object_or_404(Course, c_id=c_id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            student = form.save()
            course.enrollment.add(student)
            return redirect('course_detail', c_id = course.c_id)
        else:
            form = RegistrationForm()
            return render(request, 'registration_form.html', {'course':course, 'form' : form})
    else:
        form = RegistrationForm()
        return render(request, 'registration_form.html', {'course':course, 'form' : form})