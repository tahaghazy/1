from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.utils.text import slugify
from django.db import models

def arabic_slugify(str):
    str = str.replace(" ", "-")
    str = str.replace(",", "-")
    str = str.replace("(", "-")
    str = str.replace(")", "")
    str = str.replace("؟", "")
    return str


class Category(models.Model):
    title = models.CharField(default='category',max_length=255, verbose_name="الصف الدراسي",help_text='قم بادخال اسم الصف الدراسي')
    slug = models.SlugField(blank=True,null=True,unique=True,allow_unicode=True,help_text='يفضل تركه فارغا')
    class Meta:
        verbose_name = ('الصف الدراسي')
        verbose_name_plural = ('الصفوف الدراسيه')
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if not self.slug:
                self.slug = arabic_slugify(self.title)
        super(Category,self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class SecondCategory(models.Model):
    title = models.CharField(default='SecondCategory',max_length=255, verbose_name="الفصل الدراسي",help_text='قم بادخال اسم الفصل الدراسي')
    slug = models.SlugField(blank=True,null=True,unique=True,allow_unicode=True,help_text='يفضل تركه فارغا')
    class Meta:
        verbose_name = ('الفصل الدراسي')
        verbose_name_plural = ('الفصول الدراسيه')
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if not self.slug:
                self.slug = arabic_slugify(self.title)
        super(SecondCategory,self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100,verbose_name='العنوان',help_text='قم بادخال عنوان الدرس')
    content = models.TextField(verbose_name='الوصف',help_text='قم بادخال الوصف')
    rate = models.FloatField(max_length=3,null=True,blank=True,verbose_name='التقيم',help_text='قم بادخال تقييم الدرس')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True,related_name='posts', verbose_name="الصف الدراسي",help_text='قم باختيار اسم الصف الدراسي')
    second_category = models.ForeignKey(SecondCategory, on_delete=models.CASCADE,blank=True,null=True,related_name='posts', verbose_name="الفصل الدراسي",help_text='قم باختيار  الفصل الدراسي')
    slug = models.SlugField(blank=True,null=True,unique=True,allow_unicode=True,help_text='يفضل تركه فارغا')
    post_date = models.DateTimeField(default=timezone.now,help_text='يفضل تركه كما هو',verbose_name='تاريخ الدرس')
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='المستخدم')
    embed_code = models.CharField(max_length=300, blank=True,help_text='(قم بلصق كود التضمين لعرض المحتوي الذي تريده(فيديو يوتيوب',verbose_name='رابط التضمين')
    image = models.ImageField(default="profile_pics/def.jpg" ,upload_to='profile_pics' , blank=True,verbose_name='الصوره')
    active = models.BooleanField(default=False,verbose_name='تفعيل')
    views = models.PositiveIntegerField(default=0,help_text='يفضل تركه فارغا',verbose_name='المشاهدات')

    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url



    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if not self.slug:
                self.slug = arabic_slugify(self.title)
        super(Post,self).save(*args, **kwargs)



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/detail/{self.slug}'

    class Meta:
        ordering = ('-post_date',)
        verbose_name = ('المنشور')
        verbose_name_plural = ('المنشورات')


class Post_Altermative(models.Model):
    PALN_Post = models.ForeignKey(Post, on_delete=models.CASCADE,blank=True,null=True,related_name="main_post")
    PALN_Altermative = models.ManyToManyField(Post,related_name='altermative_post')
    class Meta:
        verbose_name = ('Post Altermative')
        verbose_name_plural = ('Post Altermatives')




class Comment(models.Model):
    name = models.CharField(max_length=50, verbose_name='الاسم')
    email = models.EmailField(verbose_name='البريد الإلكتروني')
    body = models.TextField(verbose_name='التعليق')
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.body

    class Meta:
        ordering = ('-comment_date',)
        verbose_name = ('التعليق')
        verbose_name_plural = ('التعليقات')

class Feedback(models.Model):
    name = models.CharField(max_length=200, help_text="اسم المرسل")
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "الرسائل"

    def __str__(self):
        return self.message

class About(models.Model):
    content = models.TextField()
    def __str__(self):
        return self.content

    class Meta:
        verbose_name = ('وصف الموقع')
        verbose_name_plural = ('وصف الموقع')


