# Generated by Django 5.0.8 on 2024-08-18 18:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_about_customuser_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='description',
            field=ckeditor.fields.RichTextField(default='something about me'),
        ),
    ]
