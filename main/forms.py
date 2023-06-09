from django import forms
from .models import UserProfile, Course


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class CourseForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('students', 'Студентам'),
        ('ege', 'Подготовка к ЕГЭ'),
    ]

    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=True)
    image = forms.ImageField(required=True)

    class Meta:
        model = Course
        fields = ['title', 'description', 'category', 'image']

