# Generated by Django 2.1.15 on 2020-07-25 13:22

from django.db import migrations
import django_resized.forms
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200725_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', keep_meta=True, null=True, quality=75, size=[128, 128], upload_to=users.models.user_directory_path),
        ),
    ]