# Generated by Django 5.1 on 2024-08-25 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sondages', '0007_delete_methode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='message',
            new_name='adresse',
        ),
    ]