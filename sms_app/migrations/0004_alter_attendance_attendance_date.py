# Generated by Django 4.1.6 on 2023-04-17 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0003_alter_leavereportstudent_leave_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attendance_date',
            field=models.DateField(),
        ),
    ]
