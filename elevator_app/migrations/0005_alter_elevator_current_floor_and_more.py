# Generated by Django 5.0.1 on 2024-01-05 11:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elevator_app', '0004_alter_elevator_current_floor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elevator',
            name='current_floor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current', to='elevator_app.floor'),
        ),
        migrations.AlterField(
            model_name='elevator',
            name='user_requests',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request', to='elevator_app.floor'),
        ),
    ]