from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Mets:
        model = User
        fields = ['userename', 'password1', 'password2']
        