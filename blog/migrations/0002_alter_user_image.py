# Generated by Django 5.0.6 on 2024-05-29 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='profile_pics/default.jpeg', null=True, upload_to='profile_pics/'),
        ),
    ]
