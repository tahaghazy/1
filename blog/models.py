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
    title = models.CharField(default='category',max_length=255, verbose_name="Title")
    parent = models.ForeignKey('self',limit_choices_to={'parent__isnull':True}, on_delete=models.CASCADE,blank=True,null=True)
    slug = models.SlugField(blank=True,null=True,unique=True,allow_unicode=True)
    class Meta:
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if not self.slug:
                self.slug = arabic_slugify(self.title)
        super(Category,self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class SecondCategory(models.Model):
    title = models.CharField(default='SecondCategory',max_length=255, verbose_name="Title")
    parent = models.ForeignKey('self',limit_choices_to={'parent__isnull':True}, on_delete=models.CASCADE,blank=True,null=True)
    slug = models.SlugField(blank=True,null=True,unique=True,allow_unicode=True)
    class Meta:
        verbose_name = ('SecondCategory')
        verbose_name_plural = ('SecondCategories')
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if not self.slug:
                self.slug = arabic_slugify(self.title)
        super(SecondCategory,self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    rate = models.FloatField(max_length=3,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True,related_name='posts')
    second_category = models.ManyToManyField(SecondCategory,blank=True,related_name='posts')
    slug = models.SlugField(blank=True,null=True,unique=True,allow_unicode=True)
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    embed_code = models.CharField(max_length=300, blank=True)
    image = models.ImageField(default="profile_pics/def.jpg" ,upload_to='profile_pics' , blank=True)
    active = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)



    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if not self.slug:
                self.slug = arabic_slugify(self.title)
        super(Post,self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.width > 650:
            output_size = (650,650)
            img.thumbnail(output_size)
            img.save(self.image.path)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/detail/{self.slug}'

    class Meta:
        ordering = ('-post_date',)


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




