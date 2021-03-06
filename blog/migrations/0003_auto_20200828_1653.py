# Generated by Django 3.0.9 on 2020-08-28 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20200828_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='اسم المرسل', max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'الرسائل',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'الصف الدراسي', 'verbose_name_plural': 'الصفوف الدراسيه'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-comment_date',), 'verbose_name': 'التعليق', 'verbose_name_plural': 'التعليقات'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-post_date',), 'verbose_name': 'المنشور', 'verbose_name_plural': 'المنشورات'},
        ),
        migrations.AlterModelOptions(
            name='secondcategory',
            options={'verbose_name': 'الفصل الدراسي', 'verbose_name_plural': 'الفصول الدراسيه'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='secondcategory',
            name='parent',
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, help_text='يفضل تركه فارغا', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(default='category', help_text='قم بادخال اسم الصف الدراسي', max_length=255, verbose_name='الصف الدراسي'),
        ),
        migrations.AlterField(
            model_name='post',
            name='active',
            field=models.BooleanField(default=False, verbose_name='تفعيل'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='المستخدم'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, help_text='قم باختيار اسم الصف الدراسي', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.Category', verbose_name='الصف الدراسي'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(help_text='قم بادخال الوصف', verbose_name='الوصف'),
        ),
        migrations.AlterField(
            model_name='post',
            name='embed_code',
            field=models.CharField(blank=True, help_text='(قم بلصق كود التضمين لعرض المحتوي الذي تريده(فيديو يوتيوب', max_length=300, verbose_name='رابط التضمين'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='profile_pics/def.jpg', upload_to='profile_pics', verbose_name='الصوره'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='يفضل تركه كما هو', verbose_name='تاريخ الدرس'),
        ),
        migrations.AlterField(
            model_name='post',
            name='rate',
            field=models.FloatField(blank=True, help_text='قم بادخال تقييم الدرس', max_length=3, null=True, verbose_name='التقيم'),
        ),
        migrations.AlterField(
            model_name='post',
            name='second_category',
            field=models.ForeignKey(blank=True, help_text='قم باختيار  الفصل الدراسي', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.SecondCategory', verbose_name='الفصل الدراسي'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, help_text='يفضل تركه فارغا', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='قم بادخال عنوان الدرس', max_length=100, verbose_name='العنوان'),
        ),
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(default=0, help_text='يفضل تركه فارغا', verbose_name='المشاهدات'),
        ),
        migrations.AlterField(
            model_name='secondcategory',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, help_text='يفضل تركه فارغا', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='secondcategory',
            name='title',
            field=models.CharField(default='SecondCategory', help_text='قم بادخال اسم الفصل الدراسي', max_length=255, verbose_name='الفصل الدراسي'),
        ),
    ]
