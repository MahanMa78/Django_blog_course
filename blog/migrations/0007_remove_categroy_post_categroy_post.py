# Generated by Django 5.0.8 on 2024-08-11 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_categroy_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categroy',
            name='post',
        ),
        migrations.AddField(
            model_name='categroy',
            name='post',
            field=models.ManyToManyField(null=True, related_name='+', to='blog.post'),
        ),
    ]
