# Generated by Django 4.1 on 2022-08-12 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FamilyMembersApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='familymember',
            name='birthdate',
            field=models.DateTimeField(null=True),
        ),
    ]
