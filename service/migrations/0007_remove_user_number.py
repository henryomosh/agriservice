# Generated by Django 3.2.9 on 2022-02-04 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_alter_user_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='number',
        ),
    ]
