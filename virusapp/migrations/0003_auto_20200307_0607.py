# Generated by Django 3.0.2 on 2020-03-07 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virusapp', '0002_remove_person_age_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='sick_frequency',
            field=models.CharField(max_length=30),
        ),
    ]
