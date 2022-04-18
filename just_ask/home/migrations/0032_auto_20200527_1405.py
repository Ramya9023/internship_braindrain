# Generated by Django 2.2 on 2020-05-27 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_auto_20200527_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='followers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='follow', to='home.UserProfile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='following',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followings', to='home.UserProfile'),
        ),
    ]