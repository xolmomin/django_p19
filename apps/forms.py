from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.forms import ModelForm


class RegisterModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'password', 'email']

    def clean_password(self):
        return make_password(self.cleaned_data.get('password'))
