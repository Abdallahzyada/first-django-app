# Generated by Django 4.2.6 on 2023-10-16 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authan', '0003_rename_first_name_user_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='MYUser',
        ),
    ]
