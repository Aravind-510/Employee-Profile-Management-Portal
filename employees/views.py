from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/list.html', {'employees': employees})


def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()

    return render(request, 'employees/create.html', {'form': form})


def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)
    return render(request, 'employees/detail.html', {'employee': employee})


def employee_update(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'employees/update.html', {'form': form})


def employee_delete(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        employee.delete()
        return redirect('employee_list')

    return render(request, 'employees/delete.html', {'employee': employee})

