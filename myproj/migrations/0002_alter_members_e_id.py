# Generated by Django 5.0 on 2023-12-13 07:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproj', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='e_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='myproj.employee'),
        ),
    ]