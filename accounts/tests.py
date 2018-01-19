from django.test import TestCase
from django import forms
from django.conf import settings
from .forms import UserRegistrationForm

class TestRegistrationForm(TestCase):

    def test_if_user_can_register(self):
        form = UserRegistrationForm({
            'username': 'NewUser',
            'email': 'user@user.com',
            'password1': 'Pa55w0rd',
            'password2': 'Pa55w0rd',
        })
        self.assertTrue(form.is_valid())
        

    def test_form_fails_without_email(self):
        form = UserRegistrationForm({
            'username': 'NewUser',
            'password1': 'Pa55w0rd',
            'password2': 'Pa55w0rd',
        })
        self.assertFalse(form.is_valid())