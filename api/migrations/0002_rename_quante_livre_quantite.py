# Generated by Django 3.2.4 on 2021-08-15 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livre',
            old_name='quante',
            new_name='quantite',
        ),
    ]
