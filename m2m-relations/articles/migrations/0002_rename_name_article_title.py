# Generated by Django 4.2.4 on 2023-10-02 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='name',
            new_name='title',
        ),
    ]
