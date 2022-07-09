# Overview

So far, I have learned the three main components that run the front-end for 
applications: HTML, CSS, and JavaScript. In my goal to become a full stack 
developer, I decided to learn about the Django framework for Python that can 
process requests on the back-end.

The paradigm that is used for Django is MVT. Each of these are:

1. Model - The classes, or _models_, that defines the data.
2. View - Processes the data that is to be used in the HTML template and 
renders it to the template.
3. Template - the template HTML file that is populated with data created 
by the Python functions in views.

MVC is more recognized in other back-end frameworks, however, where the 
"C" means:
- Controller – to control the operation, i.e. the URLs. Passes off to view.
Django has this respective urls.py file as well.

Instructions for making and successfully migrating the models:

- Make the model in the models.py file
- Make the migrations from the terminal: `python3 models.py makemigrations`
- Inject the migrations from the terminal: `python3 models.py migrate`

# TODO APP

The specific app that I made was a simple yet effective To-Do app that allows 
the user to enter tasks they need to complete, set the time for completion, as 
well as add specific steps for each todo. Clicking on each task will display 
the task name as well as each associated step in order. The user can then
decide to pass off each step one by one or simply mark the whole task as 
completed. The user will also be notified if a task is overdue.

This app will help me and anyone else stay on top of their daily duties.

In order to successfully test run the app, ensure that Django is installed
on your local machine and run the following command:
`python3 manage.py runserver`

Then, ctrl click the port that is shown in the terminal, and then navigate
to the homepage by adding /todo/ at the end of the url in the browser.


[Software Demo Video]https://youtu.be/GxdSa0qcI-s)

# Web Pages Created

In my todo app, three web pages are created dynamically, with the following 
names:
1. index - the homepage that dynamically displays all of the tasks found 
in the database. Each task has a link that can be clicked to access its 
associated steps page. A button on the bottom of the page takes the user
to the add_todo page.
2. add_todo - This page allows the user to create a new task with its 
associated due date/time and steps (if any). The page can update to add
additional text fields for adding more steps. These are then recorded in
the database. A return button is available to take the user back to the 
homepage.
3. steps - This page allows the user to mark individual steps or entire 
tasks as completed. Remaining steps are automatically updated. A return 
button is available to take the user back to the homepage.

Web pages are transitioned through either a hyper link reference or a
form action, which navigates like this: urls -> views -> populated
HTML template.

# Development Environment

Developed with the Django library in Python installed in a virtual environment.

Steps:

1. Create a virtual environment: 'python3 -m venv venv'
2. Activate the virtual environment: 'source venv/bin/activate'
3. Install Django: `pip install Django`

# Useful Websites

* [Django official tutorial](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)
* [Using the "name" property for data to be submitted in forms](https://stackoverflow.com/questions/14853779/adding-input-elements-dynamically-to-form)
* [Converting strings to datetime format](https://stackoverflow.com/questions/466345/converting-string-into-datetime)

# Future Work

* Beautifying the UI with more CSS
* Expand upon this idea to create a grocery list that pulls grocery items along with their respective prices from a website
* Discover how to publish the website for others to use
* Create tests for my web page in Django