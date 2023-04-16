# Newspaper agency

This is a Django pet project for managing an editorial team to store articles and track who wrote what.
The database is based on three interconnected models: Newspapers, Topics, and Redactors.
Each topic can have several newspapers, each newspaper can have several redactors, and each redactor can work on several newspapers.


## Features

* Authentication functionality for Redactor/User
* Managing newspaper redactors and topics directly from website interface (Create / Update / Delete all data) 
* Powerful admin panel for advanced managing

## Check it out

[https://newspapers-agency.onrender.com](https://newspapers-agency.onrender.com)
 
```shell
# authentication to view capabilities
username: user
password: poi123123
```

## Installation 
Python3 must be installed

A quick introduction of the minimal setup you need to get a Newspaper agency up &
running.

```shell
git clone https://github.com/inrock1/newspaper_agency
python -m venv venv
venv\Scripts\activate # (on Windows)
source venv/bin/activate # (on macOS)
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver # starts Django Server
```


## Demo
![img_2.png](./static/img_for_readme/img_2.png)

![img.png](./static/img_for_readme/img.png)

![img_1.png](./static/img_for_readme/img_1.png)


Thanks to [appseed.us](href="https://appseed.us) for frontend template.