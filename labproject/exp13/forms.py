from django import forms

class StudentSearchForm(forms.Form):
    search_term = forms.CharField(max_length=100, required=True, label='Search Student')
