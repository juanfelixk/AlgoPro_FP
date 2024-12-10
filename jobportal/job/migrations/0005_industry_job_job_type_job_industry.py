# Generated by Django 5.1.4 on 2024-12-10 05:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_applyjob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(blank=True, choices=[('Remote', 'Remote'), ('Onsite', 'Onsite'), ('Hybrid', 'Hybrid')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='industry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='job.industry'),
        ),
    ]
