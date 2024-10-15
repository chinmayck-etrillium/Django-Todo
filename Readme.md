# Todo Management with User Authentication & Authorization

In this Todo Management in made using Django and in this todo management a user can register, login and then they can add, view pending todo/ completed todo, update todo and delete todo.
As the todo management is secure, only the authenticated and authorized user can perform all the operations.

## Installation

1. Clone the repository
2. Create a python virtual environment by running script
   ```properties 
        python -m venv venv-name
        ```
3. Activate the venv
   `bash venv/Scripts/activate`
4. Install django in the virtual environment
   `bash pip install django`
5. Make migrations for the model to register
   `bash py manage.py makemigrations`
6. Migrate to save the changes
   `bash py manage.py migrate`
7. Finally run the server
   `bash py manage.py runserver`

## Key Features

- **User Registration**:

  - New user can be registered.

- **User Login**:

  - Registered users can login using credentials.

- **CRUD Todos**:

  - Only the authenticated and authorizsed can create/view/update or delete the todos.

- **Logout**:
  - The users can logout after the complete their operations.

## Technologies Used

- **Django**
- **Python**
- **Sqllite3 as DB**

### Modules in django used

- **redirect, get_object_or_404** from django.shortcuts
- **UserCreationForm, AuthenticationForm** from django.contrib.auth.forms
- **User** from django.contrib.auth.models
- **login,logout, authenticate** from django.contrib.auth
- **IntegrityError** from django.db
- **timezone**from django.utils
- **login_required** from django.contrib.auth.decorators
- **ModelForm** from django.forms

### Custom Login Url used

- **LOGIN_URL** for login_required module

## **Please Note**: This is just a working model, styling can be done as requirement.
