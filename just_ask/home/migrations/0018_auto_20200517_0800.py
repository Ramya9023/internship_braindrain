# Generated by Django 2.2 on 2020-05-17 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20200517_0758'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='ans_user',
            new_name='user',
        ),
    ]