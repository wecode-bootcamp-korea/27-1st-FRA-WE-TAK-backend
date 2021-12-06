import re

from django.core.exceptions import ValidationError

def email_check(email):
    if not re.match('^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$', email):
        raise ValidationError("email_error")

def password_check(password):
    if not re.match('^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}$', password):
        raise ValidationError("password_error")
