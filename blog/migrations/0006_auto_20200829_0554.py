# Generated by Django 3.0.9 on 2020-08-29 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200828_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scripts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='اسم السكربت ')),
                ('script', models.TextField(help_text='(قم باضافة السكربت الذي تريده هنا مثل(كود تفعيل ادسنس ', verbose_name='السكربت')),
            ],
            options={
                'verbose_name': 'اضافة سكربت للموقع',
                'verbose_name_plural': 'اضافة سكربت للموقع',
            },
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=200, verbose_name='اسم المرسل'),
        ),
    ]
