# Generated by Django 4.1 on 2022-08-12 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FamilyMembersApp', '0002_familymember_birthdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='familymember',
            old_name='birthdate',
            new_name='createdAt',
        ),
    ]