# Generated by Django 3.2.2 on 2021-06-06 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prescriptions', '0002_remove_prescription_drugs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='drug_data',
        ),
    ]
