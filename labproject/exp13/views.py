from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from exp12.models import Student 
from .forms import StudentSearchForm  

def search_page(request):
    form = StudentSearchForm()
    return render(request, 'search_page.html', {'form': form})

def search_student(request):
    if request.method == 'GET' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        search_term = request.GET.get('search_term', None)
        if search_term:
            # Create a query to search for the full name
            query = Q(first_name__icontains=search_term) | Q(last_name__icontains=search_term)
            full_name_query = Q(first_name__icontains=search_term) | Q(last_name__icontains=search_term)
            search_terms = search_term.split()
            if len(search_terms) > 1:
                full_name_query = Q(first_name__icontains=search_terms[0]) & Q(last_name__icontains=search_terms[1])
                query = query | full_name_query

            students = Student.objects.filter(query).distinct()
            student_data = [
                {
                    'name': f"{student.first_name} {student.last_name}",
                    'courses': [course.name for course in student.courses.all()]
                } for student in students
            ]
            return JsonResponse({'students': student_data})
    return JsonResponse({'students': []})
