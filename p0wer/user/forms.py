from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



class UsercreationForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False, help_text='', label='اسم المستخدم')
    first_name = forms.CharField(max_length=30, required=False, help_text='', label='الاسم الأول')
    last_name = forms.CharField(max_length=30, required=False, help_text='', label='الاسم الأخير')
    email = forms.EmailField(max_length=254, help_text='قم بادخال بريدك الالكتروني علي سبيل المثال name@example.com.',
                             label='البريد الالكتروني')
    password1 = forms.CharField(max_length=30, required=False,
                                help_text='استخدم 8 أحرف أو أكثر مع مزيج من الأحرف والأرقام والرموز.',
                                label='كلمة المرور', widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(max_length=30, required=False, help_text='قم بكتابة نفس كلمة المرور السابقه.',
                                label='تأكيد كلمة المرور', widget=forms.PasswordInput(), min_length=8)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('كلمة المرور غير متطابقة')
        return cd['password2']

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('يوجد مستخدم مسجل بهذا الاسم.')
        return cd['username']


class LoginForm(forms.ModelForm):
    username = forms.CharField(label='اسم المستخدم')
    password = forms.CharField(
        label='كلمة المرور', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='', label='الاسم الأول')
    last_name = forms.CharField(max_length=30, required=False, help_text='', label='الاسم الأخير')
    email = forms.EmailField(max_length=254, help_text='قم بادخال بريدك الالكتروني علي سبيل المثال name@example.com.',
                             label='البريد الالكتروني')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')




class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)
