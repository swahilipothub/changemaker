# Generated by Django 2.1.15 on 2020-07-25 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20200725_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending Approval'), ('APPROVED', 'Approved'), ('CANCELLED', 'Cancelled')], default='PENDING', max_length=32),
        ),
    ]