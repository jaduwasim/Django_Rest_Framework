from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    
    def clean_esal(self):
        inpusal = self.cleaned_data['esal']
        if inpusal < 5000:
            raise forms.ValidationError('Salary Shold be Grater Equeal Five Thousend')
        return inpusal

    class Meta:
        model = Employee
        fields = '__all__'