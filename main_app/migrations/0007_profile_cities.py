# Generated by Django 4.2.1 on 2023-06-12 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_log_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cities',
            field=models.ManyToManyField(to='main_app.city'),
        ),
    ]
