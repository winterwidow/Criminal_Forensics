# Generated by Django 4.2 on 2023-06-03 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_member_dna'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='dna',
            new_name='cr_dna',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='firstname',
            new_name='cr_firstname',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='lastname',
            new_name='cr_lastname',
        ),
    ]
