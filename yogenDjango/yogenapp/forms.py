from django import forms
from django.core import validators
from yogenapp.models import Users,UserProfileInfo
from django.contrib.auth.models import User

class FormView(forms.Form):
    name=forms.CharField(validators=[validators.MaxLengthValidator(4)])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Confirm Email")
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']
        verifymail = cleaned_data['verify_email']
        if email != verifymail:
            raise forms.ValidationError("Emails should Match")

class NewUserForm(forms.ModelForm):
    class Meta():
        model = Users
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
