# Generated by Django 4.0.6 on 2022-09-20 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.FloatField()),
                ('revenue', models.FloatField()),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('profit', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='DailyPerformance',
            fields=[
                ('performance_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backend.performance')),
                ('date', models.DateField(auto_now_add=True)),
            ],
            bases=('backend.performance',),
        ),
        migrations.CreateModel(
            name='HourlyPerformance',
            fields=[
                ('performance_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backend.performance')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
            bases=('backend.performance',),
        ),
    ]
