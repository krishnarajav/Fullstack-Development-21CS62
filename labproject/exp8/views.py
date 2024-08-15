from django.shortcuts import render, get_object_or_404
from exp7.models import Course

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courselist.html', {'courses':courses})

def course_detail(request, c_id):
    course = get_object_or_404(Course, c_id=c_id)
    students = course.enrollment.all()
    return render(request, 'coursedetail.html', {'course': course, 'students': students})   