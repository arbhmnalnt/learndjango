# Generated by Django 4.0.6 on 2022-09-22 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_attendance_employee_attendance_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='employee',
        ),
        migrations.AddField(
            model_name='attendance',
            name='employees',
            field=models.ManyToManyField(related_name='employees', to='store.employee'),
        ),
    ]
