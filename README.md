# UserManagementAPI

This is a Django project that overrides the default user model, and implements
a user management API using the Django Rest Framework.

Python version: 3.10.18\
Django version: 4.2

### To get started:

Create virtual environment:
```
python -m venv venv
pip install --upgrade pip
```
Install requirements:
```
pip install -r requirements.txt
```
Start server:
```
python manage.py runserver
```

### curl api calls:
```
curl http://127.0.0.1:8000/users/
```
```
curl -d '{"password": "p1p2p3p4a1a2a3a4", "username": "randus", "email": "ru@g.com"}' -H "Content-Type: application/json" -X Post  http://127.0.0.1:8000/users/
```