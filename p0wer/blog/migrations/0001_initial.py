# Generated by Django 3.0.9 on 2020-08-22 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='category', max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True, unique=True)),
                ('parent', models.ForeignKey(blank=True, limit_choices_to={'parent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('rate', models.FloatField(blank=True, max_length=3, null=True)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True, unique=True)),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('post_update', models.DateTimeField(auto_now=True)),
                ('embed_code', models.CharField(blank=True, max_length=300)),
                ('image', models.ImageField(blank=True, default='profile_pics/def.jpg', upload_to='profile_pics')),
                ('active', models.BooleanField(default=False)),
                ('views', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.Category')),
            ],
            options={
                'ordering': ('-post_date',),
            },
        ),
        migrations.CreateModel(
            name='SecondCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='SecondCategory', max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True, unique=True)),
                ('parent', models.ForeignKey(blank=True, limit_choices_to={'parent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.SecondCategory')),
            ],
            options={
                'verbose_name': 'SecondCategory',
                'verbose_name_plural': 'SecondCategories',
            },
        ),
        migrations.CreateModel(
            name='Post_Altermative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PALN_Altermative', models.ManyToManyField(related_name='altermative_post', to='blog.Post')),
                ('PALN_Post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_post', to='blog.Post')),
            ],
            options={
                'verbose_name': 'Post Altermative',
                'verbose_name_plural': 'Post Altermatives',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='second_category',
            field=models.ManyToManyField(blank=True, related_name='posts', to='blog.SecondCategory'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='الاسم')),
                ('email', models.EmailField(max_length=254, verbose_name='البريد الإلكتروني')),
                ('body', models.TextField(verbose_name='التعليق')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post')),
            ],
            options={
                'ordering': ('-comment_date',),
            },
        ),
    ]
