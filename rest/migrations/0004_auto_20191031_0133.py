# Generated by Django 2.1.4 on 2019-10-30 16:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rest', '0003_album_files'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Files',
            new_name='File',
        ),
    ]
