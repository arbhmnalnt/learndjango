# Generated by Django 4.0.6 on 2022-09-22 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_employee_dateofemployment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='eNum',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='الرقم التعريفى'),
        ),
    ]
