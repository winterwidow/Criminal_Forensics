# Generated by Django 4.2 on 2023-08-19 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_member_cr_crime_member_cr_date_member_cr_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='cr_crime',
            field=models.CharField(db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='cr_date',
            field=models.DateField(db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='cr_firstname',
            field=models.CharField(db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='cr_gender',
            field=models.CharField(db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='cr_lastname',
            field=models.CharField(db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='cr_weapon',
            field=models.CharField(db_index=True, max_length=255, null=True),
        ),
    ]
