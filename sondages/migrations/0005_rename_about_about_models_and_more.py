# Generated by Django 5.1 on 2024-08-23 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sondages', '0004_rename_image_service_images_alter_contact_nom'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='about',
            new_name='about_models',
        ),
        migrations.RenameField(
            model_name='about_models',
            old_name='title',
            new_name='title_about',
        ),
    ]