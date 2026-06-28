from django import forms
from .models import Employee
from datetime import date
import re

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'

    # Employee ID Validation
    def clean_employee_id(self):
        employee_id = self.cleaned_data['employee_id']

        if not re.match(r'^EMP\d+$', employee_id):
            raise forms.ValidationError(
                "Employee ID must be like EMP001"
            )

        return employee_id

    # Email Validation
    def clean_email(self):
        email = self.cleaned_data['email']

        if Employee.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Email already exists"
            )

        return email

    # Phone Validation
    def clean_phone(self):
        phone = self.cleaned_data['phone']

        if not phone.isdigit():
            raise forms.ValidationError(
                "Phone must contain only digits"
            )

        if len(phone) != 10:
            raise forms.ValidationError(
                "Phone number must be 10 digits"
            )

        return phone

    # Salary Validation
    def clean_salary(self):
        salary = self.cleaned_data['salary']

        if salary < 10000:
            raise forms.ValidationError(
                "Minimum salary is 10000"
            )

        if salary > 500000:
            raise forms.ValidationError(
                "Maximum salary is 500000"
            )

        return salary

    # Joining Date Validation
    def clean_joining_date(self):
        joining_date = self.cleaned_data['joining_date']

        if joining_date > date.today():
            raise forms.ValidationError(
                "Joining date cannot be a future date"
            )

        return joining_date