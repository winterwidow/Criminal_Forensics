# Generated by Django 4.2 on 2023-08-17 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_remove_member_cr_dna'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='cr_crime',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='cr_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='cr_gender',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='cr_weapon',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='cr_firstname',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='cr_lastname',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
