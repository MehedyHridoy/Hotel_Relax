# Generated by Django 4.2.6 on 2023-10-26 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='fImage',
            new_name='image',
        ),
    ]
