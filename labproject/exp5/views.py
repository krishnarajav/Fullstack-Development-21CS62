from django.shortcuts import render

def fruitslist(request):
    fruits = ['Apple', 'Banana', 'Orange', 'Mango', 'Pineapple']
    context = {
        'fruits': fruits,
    }
    return render(request, 'fruitslist.html', context)

def studentslist(request):
    students = ['John', 'Jane', 'Mike', 'Sarah', 'Tom']
    context = {
        'students': students,
    }
    return render(request, 'studentslist.html', context)

#def error_404(request, exception):
    #return render(request, '404.html', status=404)