# Generated by Django 4.2.7 on 2023-11-21 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='Anonymous', max_length=100),
        ),
    ]
