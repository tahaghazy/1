from django import forms
from .models import Comment, Post

class NewComment(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name','email','body')


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(label='عنوان التدوينة')
    content = forms.CharField(label='نص التدوينة', widget=forms.Textarea)
    embed_code = forms.CharField(label='رمز التضمين',required=False ,help_text = 'قم بتضمين محتوى خارجي')

    class Meta:
        model = Post
        fields = ['title', 'content','embed_code']

class ContactForm(forms.Form):
    subject = forms.CharField(required=True,label='الاسم')
    from_email = forms.EmailField(required=True ,label='البريد الالكتروني')
    message = forms.CharField(widget=forms.Textarea, required=True,label='محتوي الرساله')