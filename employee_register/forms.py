from django import forms
from .models import Employee  ## import the Employee models field

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        ## '__all__' it will take all
        #fields = '__all__'  ## All Properties of Employee model's as field, we can get by using this.
        # Customize (if i want then i can remove or can take all)
        fields = ('fullname', 'mobile', 'emp_code', 'position')
        labels = {             ## To Update the label text
            'fullname': 'Full Name',
            'emp_code': 'EMP. Code'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False  # removed required validation for EMP. Code
