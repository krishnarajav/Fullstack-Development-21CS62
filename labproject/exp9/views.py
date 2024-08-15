from django.shortcuts import render, redirect
from .forms import ProjectForm

def project_submission(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_success')  # Redirect to a success page
    else:
        form = ProjectForm()
    return render(request, 'project_form.html', {'form': form})

