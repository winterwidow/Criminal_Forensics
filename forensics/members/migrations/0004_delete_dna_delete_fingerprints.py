# Generated by Django 4.2 on 2023-05-01 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_dna'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DNA',
        ),
        migrations.DeleteModel(
            name='fingerprints',
        ),
    ]
