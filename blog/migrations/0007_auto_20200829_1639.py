# Generated by Django 3.0.9 on 2020-08-29 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200829_0554'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThirdCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='الموضوع', help_text='قم بادخال اسم  الموضوع', max_length=255, verbose_name='الموضوع')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, help_text='يفضل تركه فارغا', null=True, unique=True)),
            ],
            options={
                'verbose_name': 'الموضوع',
                'verbose_name_plural': 'المواضيع',
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(default='الصف', help_text='قم بادخال اسم الصف الدراسي', max_length=255, verbose_name='الصف الدراسي'),
        ),
        migrations.AlterField(
            model_name='secondcategory',
            name='title',
            field=models.CharField(default='الفص', help_text='قم بادخال اسم الفصل الدراسي', max_length=255, verbose_name='الفصل الدراسي'),
        ),
    ]