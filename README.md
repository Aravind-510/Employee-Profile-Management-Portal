Company Portal – Employee Management System
A Django-based Employee Profile Management Portal covering all modules from the assignment.
________________________________________
Features
•	Employee CRUD (Create, Read, Update, Delete)
•	Form Validation (Employee ID format, unique email, salary range, phone 10 digits, no future joining date)
•	Profile Image Upload
•	Search (by ID, Name, Email, Department)
•	Filter (by Department, Status)
•	Pagination (10 per page)
•	Django Messages Framework
•	Both FBV and CBV implementations
________________________________________
Setup & Run

# 1. Clone the repositary


# 2. Move into the Project Folder
Cd Employee Profile Management

# 3. Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run migrations
python manage.py makemigrations
python manage.py migrate

# 6. Create superuser (optional)
python manage.py createsuperuser

# 7. Start development server
python manage.py runserver

# 8. Open in browser
# http://127.0.0.1:8000/
# Admin: http://127.0.0.1:8000/admin/
________________________________________


URL Reference
URL	Description
/	Employee List
/employees/create/	Add Employee
/employees/<id>/	Employee Detail
/employees/update/<id>/	Update Employee
/employees/delete/<id>/	Delete Employee
/admin/	Django Admin
________________________________________
Validation Rules
Field	Rule
Employee ID	Format: EMP + digits (EMP001), must be unique
Email	Valid format, must be unique
Phone	Exactly 10 digits
Salary	Min ₹10,000 – Max ₹5,00,000
Joining Date	Cannot be a future date
________________________________________


Project Structure
Employee Profile Management /
├── company_portal/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── employees/
│   ├── models.py
│   ├── forms.py
│   ├── views.py       # Both FBV + CBV
│   ├── urls.py
│   ├── admin.py
│   └── templates/employees/
│       ├── list.html
│       ├── create.html
│       ├── detail.html
│       ├── update.html
│       └── delete.html
├── templates/
│   └── base.html
├── media/employees/
├── manage.py
└── requirements.txt



