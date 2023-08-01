# Task Manager

Task Manager is a Django web application designed to help users manage their tasks efficiently. It allows users to create an account, log in, and add, edit, and delete tasks with full CRUD (Create, Read, Update, Delete) functionality. The application provides a user-friendly interface to manage tasks and keep track of their due dates and urgency status.

##  Requirements:

- asgiref==3.7.2
- cloudinary==1.33.0
- dj-database-url==0.5.0
- dj3-cloudinary-storage==0.0.6
- Django==3.2.20
- django-heroku==0.3.1
- gunicorn==21.2.0
- psycopg2==2.9.6
- psycopg2-binary==2.9.6
- sqlparse==0.4.4
- urllib3==1.26.16


## Usage

1. **Register User**: Users can register for an account to access the task management features.

2. **Login**: Registered users can log in to their accounts to view and manage their tasks.

3. **Home Page**: The home page displays a list of tasks for the logged-in user. If the user is not authenticated, it prompts them to log in or register to view tasks.

4. **Add Task**: Users can click the "Add A Task" button on the home page to create a new task. The "Add Task" page provides fields to input the task's title, description, due date, and urgency status.

5. **Edit Task**: On the home page, users can click the "Edit" button next to each task to modify the task's details. The "Edit Task" page displays a form with fields to update the task's title, description, due date, and urgency status.

6. **Delete Task**: On the home page, users can click the "Delete" button next to each task to remove the task from their task list.

7. **Task Urgency Toggle**: Users can toggle the urgency status of tasks (urgent/non-urgent) by clicking the "Toggle Urgency" button on the home page.

## Templates

### base.html

The `base.html` file is the base template used for rendering other HTML pages. The base.html file contains:
- The head element to hold Google Fonts, Bootstrap and custom CSS styling.
- The navigation bar. 
    - The navigation bar will change depending on if the user is logged into the site.
- The hero section. 

### add_task.html

The `add_task.html` file is the homepage template that extends the `base.html` template.
- This file allows users to create tasks through filling out a form. 

### register_user.html

The `register_user.html` file is the registration page template that extends the `base.html` template.
- This file allows users to create a new account and login to the site and see the tasks.

### edit_task.html

The `edit_task.html` file is the "Edit Task" page template that extends the `base.html` template.

### login.html

The `login.html` file is the "Login" page template that extends the `base.html` template. 
- This file allows users to login to the site using their account credentials.

## Libraries. 
In this project I used:

### Google Fonts. 
Google Font's 'Roboto' is used throughout the project.
- More information about google fonts is available here: https://fonts.google.com/

### Bootstrap.
Bootstrap features such as a responsive navbar and button styling were used in this project. 
- More information about Bootstrap is available here: https://getbootstrap.com/docs/5.3/getting-started/introduction/

## Credit 

### Code Institutes 'Hello Django' 
- Models and views from this walkthrough project were used in creating CRUD functionality. 

### Django Wednesdays
- The code for: 
    - user registration. 
    - login / logout functionality. 
    - styling Python's `{% form %}` through widgets. 
Was found in the Django Wednesdays youtube playlist which is found here: https://www.youtube.com/watch?v=HHx3tTQWUx0&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy. 

The videos which I am referring to in this playlist are linked here:
- Login : https://www.youtube.com/watch?v=CTrVDi3tt8o&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy&index=21
- Logout : https://www.youtube.com/watch?v=BTq0MAIJEH8&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy&index=22
- Registering Users : https://www.youtube.com/watch?v=EqjRhO5CK6A&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy&index=24
- Styling Forms : https://www.youtube.com/watch?v=XapMxdIyLM8&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy&index=26
