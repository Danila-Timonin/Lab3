# Generated by Django 4.2.1 on 2023-06-09 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_course_description_remove_course_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(choices=[('students', 'Студентам'), ('ege', 'Подготовка к ЕГЭ')], default='students', max_length=20),
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default='', upload_to='course_images/'),
        ),
        migrations.AddField(
            model_name='course',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
