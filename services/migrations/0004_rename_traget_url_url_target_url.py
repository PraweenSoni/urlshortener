# Generated by Django 5.0.6 on 2024-06-24 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_url_short_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='traget_url',
            new_name='target_url',
        ),
    ]
