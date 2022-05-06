# Run Project

## Setup

The first thing to do is to clone the repository:

Create a virtual environment to install dependencies in and activate it:
Make sure you have python3

```sh
$ python3 -m venv venv
$ source env/bin/activate
```

Go inside the folder using cd command and find requirements.txt file
Then install the dependencies:

```sh

(venv)$ pip install -r requirements.txt
```

Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set.

Once `pip` has finished downloading the dependencies:

```sh
(venv)$ python manage.py makemigrations
(venv)$ python manage.py migrate
(venv)$ python manage.py runserver
```

And navigate to `http://localhost:8000`.
