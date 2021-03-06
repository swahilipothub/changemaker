# Generated by Django 2.1.15 on 2020-07-21 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_auto_20200630_1059'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SMS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('number', models.CharField(max_length=13)),
                ('status', models.CharField(max_length=50)),
                ('messageId', models.CharField(max_length=256)),
                ('cost', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('changemaker', models.ManyToManyField(to='users.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'messages',
            },
        ),
    ]
