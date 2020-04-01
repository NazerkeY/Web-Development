# Generated by Django 3.0.4 on 2020-04-01 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='company',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='company_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Company'),
        ),
    ]
