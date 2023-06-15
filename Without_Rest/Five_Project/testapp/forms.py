from django import forms
from .models import Employee

class Employee_Form(forms.ModelForm):
    
    def clean_esal(self):
        inputsal = self.clean_data['esal']
        if inputsal < 5000:
            raise forms.ValidationError('Salary should greater then 5000')
        return inputsal

    class Meta:
        model = Employee
        fields = '__all__'