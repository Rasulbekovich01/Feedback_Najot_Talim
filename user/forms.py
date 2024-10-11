from user.models import User
from django import forms
from config.settings import EMAIL_DEFAULT_SENDER
from django.core.mail import send_mail
from user.custom_field import MultiEmailField
from .models import User
from .models import Problem, Offer, Comment


class LoginForm(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True)


class RegisterModelForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean_email(self):
        email = self.data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'This {email} is already registered.')
        return email

    def clean_password(self):
        password: str = self.data.get('password')
        confirm_password: str = self.data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Please enter the same password')
        return self.cleaned_data['password']

    def save(self, commit=True):
        user = super(RegisterModelForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = False
        user.is_superuser = True
        user.is_staff = True

        if commit:
            user.save()

        return user


class EmailSendForm(forms.Form):
    email = MultiEmailField(widget=forms.Textarea)
    title = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']
        email = self.cleaned_data['email']
        sender = EMAIL_DEFAULT_SENDER
        send_mail(
            title,
            message,
            sender,
            email,
            fail_silently=False,
        )

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['content', 'is_anonymous']

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['title', 'description']

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']