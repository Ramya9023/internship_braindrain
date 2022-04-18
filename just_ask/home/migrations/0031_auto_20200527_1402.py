# Generated by Django 2.2 on 2020-05-27 09:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_auto_20200527_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='followers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='following',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]