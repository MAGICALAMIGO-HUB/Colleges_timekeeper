# Generated by Django 4.1 on 2022-12-28 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeAPI', '0004_alter_user_address_alter_user_address_long_lat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]