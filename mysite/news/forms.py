from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from captcha.fields import CaptchaField

class ContactFrom(forms.Form):
    subject = forms.CharField(label='Тема', help_text='Подсказка... Максимум 150 символов',widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', help_text='Подсказка... Максимум 150 символов',widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    captcha = CaptchaField()



class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Подсказка... Максимум 150 символов', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Подсказка... Максимум 150 символов', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# 1
# from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

    # валидация тайтла
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')

        return title






# 1
# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs={"class": "form-control"}))
#     content = forms.CharField(label='Текст', required=False, widget=forms.Textarea(attrs={
#         "class": "form-control",
#         "rows": 5
#     }))
#     is_published = forms.BooleanField(label='Опубликовано', initial=True)
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Ктегория', empty_label='Выберите категорию', widget=forms.Select(attrs={
#         "class": "form-control"
#     }))