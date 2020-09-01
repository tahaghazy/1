# Generated by Django 3.0.9 on 2020-08-30 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200830_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='thirdcategory',
            name='category',
            field=models.ForeignKey(blank=True, help_text='قم باختيار اسم الصف الدراسي', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='blog.Category', verbose_name='الصف الدراسي'),
        ),
        migrations.AlterField(
            model_name='post',
            name='embed_code',
            field=models.CharField(blank=True, help_text='(قم بلصق معرف   الفيديو الذي تريده(فيديو يوتيوب', max_length=300, verbose_name='معرف الفيديو'),
        ),
    ]