from django.test import TestCase
from .models import User
from myproject.utils import PasswordTooShortException


from rest_framework.test import RequestsClient


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="user1", email="u1@g.com")
        User.objects.create(username="user2", email="u2@g.com", age="22")

    def test_post_user(self):
        users = User.objects.all()
        assert len(users) == 2

        client = RequestsClient()
        response = client.post('http://testserver/users/', {'username': 'user3', 'email': 'e3@g.com', 'password': 'p1p2p3p4a1a2a3a4'})

        assert response.status_code == 201

        users = User.objects.all()
        assert len(users) == 3

    def test_post_user_password_too_short(self):
        client = RequestsClient()
        response = client.post('http://testserver/users/', {'username': 'user3', 'email': 'e3@g.com', 'password': 'p1p'})

        assert response.status_code == 422
        assert "Password is too short" in str(response.content)
        

