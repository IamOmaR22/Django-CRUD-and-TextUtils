from django.shortcuts import render
from .forms import EmployeeForm ## Import the EmployeeForm from froms.py

# Create your views here.

def employee_list(request):
    return render(request, 'employee_register/employee_list.html')

def employee_form(request):
    form = EmployeeForm()  ## From forms.py
    return render(request, 'employee_register/employee_form.html', {'form':form})

def employee_delete(request):
    return