# Generated by Django 2.2 on 2020-05-28 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_auto_20200528_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='title',
        ),
    ]