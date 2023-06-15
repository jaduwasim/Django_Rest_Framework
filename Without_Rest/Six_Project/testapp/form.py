from typing import Any, Dict
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    def clean_esal(self):
        inputsal = self.cleaned_data['esal']
        if inputsal < 5000:
            raise forms.ValidationError('Salary Should be greate then five thousend')
        return inputsal
    class Meta:
        model = Employee
        fields = '__all__'