# CBV_To_Do_App
 <h1 align="center">Django Class Based View ToDo App</h1> 
<h2 align="center">This is a simple of a <strong>Demo Class Based View</strong> ToDoApp</h2>

### Overview
- [Overview](#overview)
- [Built With](#Built-With)
- [Demo](#demo)
- [Database schema](#database-schema)
- [Features](#features)
- [Setup](#setup)
- [Getting ready](#getting-ready)
- [options](#options)
- [Reformat and check](#reformat-and-check)
- [Todo](#todo)
- [Bugs or Opinion](#bugs-or-opinion)

### Built With
<p> This section is the list of languages used in this project.</p>
---
<p align="center" >
<img src="https://github.com/wsvincent/awesome-django/raw/main/assets/django-logo-positive.svg" alt="database schema"  margin="20px" width="70" height="70"/>
<img src="https://hugovk.github.io/python-logos/img/EuroPython%20Society.png" alt="database schema" margin="20px"  width="70" height="70"/>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg"  margin="20px" alt="bootstrap" width="70" height="70"/>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg"  margin="20px" alt="html5" width="70" height="70"/>
<img src="http://3con14.biz/code/_data/js/intro/js-logo.png" alt="js"  margin="20px" width="70" height="70"/>
<img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite"  margin="20px" width="70" height="70"/>
</p>

---

### Demo
This is a brief demo of how does project works!
<p align="center">
<img src="https://github.com/Novin1380/CBV_To_Do_App/blob/main/Demo/ToDoApp-Test.gif" alt="database schema" width="720"/>
</p>

### Database schema
A simple view of the project model schema.
<p align="center">
<img src="https://github.com/Novin1380/CBV_To_Do_App/blob/main/Demo/Data.PNG" alt="database schema" width="300"/>
</p>

### features
<h5>with these features:</h5>
 <p>1.front-end was designed by me </p>
 <p>2.backend was written by me with django 3.2</p>
 <p>3.you can add/edit/delete/complete your tasks</p>
 <p>4.tasks are personalized for the people</p>
 <p>5.its important that all pages are LoginRequire so you should create accounts to use it</p>


### Setup
To get this repository, run the following command inside your git enabled terminal
```bash
git clone https://github.com/Novin1380/CBV_To_Do_App
```

### Getting ready
Create an enviroment in order to keep the repo dependencies seperated from your local machine.
```bash
python -m venv venv
```

Make sure to install the dependencies of the project through the requirements.txt file.
```bash
pip install -r requirements.txt
```

Once you have installed django and other packages, go to the cloned repo directory and run the following command

```bash
python manage.py makemigrations
```

This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command
```bash
python manage.py migrate
```

### options
Project it self has the user creation form but still in order to use the admin you need to create a super user.you can use the createsuperuser option to make a super user.
```bash
python manage.py createsuperuser
```

And lastly let's make the App run. We just need to start the server now and then we can start using our simple todo App. Start the server by following command

```bash
python manage.py runserver
```

Once the server is up and running, head over to http://127.0.0.1:8000 for the App.

### Reformat and check
💡If you want to use this code in your project, notice that the libraries that used in this code are in requirements.txt.
💡Its important that all pages are LoginRequire so you should create accounts to test it.

### Todo
- [x] leave comments for codes
- [x] add unit tests
- [x] complete the documentation
- [x] create a video tutorial



<h3 align="center" color="red">In the future I will complete this project and make new features</h3>

<h5 align="center">just enjoy! 👋</h5>
 