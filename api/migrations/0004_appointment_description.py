# Generated by Django 5.0.5 on 2024-05-09 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_appointment_table_alter_department_table_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='description',
            field=models.TextField(default=datetime.datetime(2024, 5, 9, 13, 56, 57, 730382, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
