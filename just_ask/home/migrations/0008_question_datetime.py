# Generated by Django 2.2 on 2020-05-14 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200515_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='dateTime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
