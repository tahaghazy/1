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
    title = models.CharField(default='الصف',max_length=255, verbose_name="الصف الدراسي",help_text='قم بادخال اسم الصف الدراسي')
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
    title = models.CharField(default='الفصل',max_length=255, verbose_name="الفصل الدراسي",help_text='قم بادخال اسم الفصل الدراسي')
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

class ThirdCategory(models.Model):
    title = models.CharField(default='الماده',max_length=255, verbose_name="الماده",help_text='قم بادخال اسم  الماده')
    slug = models.SlugField(blank=True,null=True,unique=True,allow_unicode=True,help_text='يفضل تركه فارغا')
    class Meta:
        verbose_name = ('الماده')
        verbose_name_plural = ('المواد')
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if not self.slug:
                self.slug = arabic_slugify(self.title)
        super(ThirdCategory,self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class FourthCategory(models.Model):
    title = models.CharField(default='المرحله',max_length=255, verbose_name="المرحله الدراسيه",help_text='قم بادخال اسم المرحلة الدراسيه')
    slug = models.SlugField(blank=True,null=True,unique=True,allow_unicode=True,help_text='يفضل تركه فارغا')
    class Meta:
        verbose_name = ('المرحله الدراسيه')
        verbose_name_plural = ('المراحل الدراسيه')
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if not self.slug:
                self.slug = arabic_slugify(self.title)
        super(FourthCategory,self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100,verbose_name='العنوان',help_text='قم بادخال عنوان الدرس')
    content = models.TextField(verbose_name='الوصف',help_text='قم بادخال الوصف')
    rate = models.FloatField(max_length=3,null=True,blank=True,verbose_name='التقيم',help_text='قم بادخال تقييم الدرس')
    fourth_category = models.ForeignKey(FourthCategory, on_delete=models.CASCADE,blank=True,null=True,related_name='posts', verbose_name="المرحله الدراسيه",help_text='قم باختيار اسم  المرحله الدراسيه')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True,related_name='posts', verbose_name="الصف الدراسي",help_text='قم باختيار اسم الصف الدراسي')
    second_category = models.ForeignKey(SecondCategory, on_delete=models.CASCADE,blank=True,null=True,related_name='posts', verbose_name="الفصل الدراسي",help_text='قم باختيار  الفصل الدراسي')
    third_category = models.ForeignKey(ThirdCategory, on_delete=models.CASCADE,blank=True,null=True,related_name='posts', verbose_name="الماده ",help_text='قم باختيار اسم  الماده')
    slug = models.SlugField(blank=True,null=True,unique=True,allow_unicode=True,help_text='يفضل تركه فارغا')
    post_date = models.DateTimeField(default=timezone.now,help_text='يفضل تركه كما هو',verbose_name='تاريخ الدرس')
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='المستخدم')
    embed_code = models.CharField(max_length=300, blank=True,help_text='(قم بلصق معرف   الفيديو الذي تريده(فيديو يوتيوب',verbose_name='معرف الفيديو')
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
    name = models.CharField(max_length=200, verbose_name="اسم المرسل")
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




class Scripts(models.Model):
    title = models.CharField(max_length=100,verbose_name='اسم السكربت ')
    script = models.TextField(verbose_name='السكربت',help_text='(قم باضافة السكربت الذي تريده هنا مثل(كود تفعيل ادسنس ')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = ('اضافة سكربت للموقع')
        verbose_name_plural = ('اضافة سكربت للموقع')

class Banner(models.Model):
    title = models.CharField(max_length=100,verbose_name='اسم السكربت ')
    script = models.TextField(verbose_name='السكربت',help_text='(قم باضافة السكربت الذي تريده هنا مثل(كود تفعيل ادسنس ')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = ('اضافة بانر ')
        verbose_name_plural = ('اضافة بانر ')

class SlideBanner(models.Model):
    title = models.CharField(max_length=100,verbose_name='اسم السكربت ')
    script = models.TextField(verbose_name='السكربت',help_text='(قم باضافة السكربت الذي تريده هنا مثل(كود تفعيل ادسنس ')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = ('اضافة بانر جانبي')
        verbose_name_plural = ('اضافة بانر جانبي')

class Links(models.Model):
    title = models.CharField(max_length=100,verbose_name='اسم الموقع ')
    script = models.URLField(verbose_name='الرابط',help_text='قم باضافة رابط الموقع الذي تريد عرضه اسفل الموقع ')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = ('اضافة رابط للموقع')
        verbose_name_plural = ('اضافة رابط للموقع')
