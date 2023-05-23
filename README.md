# SQL Injection Template

## How to run
```bash
python -m venv env # create a virtual environment
source env/bin/activate # activate the virtual environment
pip install -r requirements.txt # download the dependencies
python seed.py # to create the database with default users
flask run # to run the
```

## How to use

Go to the [http://127.0.0.1:5000](http://127.0.0.1:5000) and enter the following credentials:

Try to login with the following credentials:

email = `admin@example.com`

password = `password`

Now try to login with the sql injection payload:

email = `' OR 1=1 --`
password = `' OR 1=1 --`


