# Generated by Django 3.2.7 on 2021-09-25 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='utl',
            new_name='url',
        ),
    ]
