from typing import Any, Dict
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    def clean_esal(self): #function Name should be cleansal other it will not call
        inputsal = self.cleaned_data['esal']
        if inputsal < 5000:
            raise forms.ValidationError('The Minimum Salary shuld be 5000')
        return inputsal

    class Meta:
        model = Employee
        fields = '__all__'