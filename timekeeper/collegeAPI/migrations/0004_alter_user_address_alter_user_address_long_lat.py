# Generated by Django 4.1 on 2022-12-28 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeAPI', '0003_rename_users_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='address_long_lat',
            field=models.TextField(),
        ),
    ]
