# Generated by Django 4.0.6 on 2022-09-20 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='profit',
            field=models.FloatField(blank=True),
        ),
    ]
