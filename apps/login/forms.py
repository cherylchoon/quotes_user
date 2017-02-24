from django import forms
from .models import User
from django.forms.widgets import SelectDateWidget


BIRTH_YEAR_CHOICES = (tuple((str(i)) for i in xrange(1950, 2017)))
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'alias', 'email', 'birthday']
        widgets = {
          'birthday': forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"), years=BIRTH_YEAR_CHOICES)
          }

    password = forms.CharField(min_length=8, max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(min_length=8, max_length=100, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError('Passwords do not match!')

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=8, max_length=100, widget=forms.PasswordInput)
