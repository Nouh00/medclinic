# Generated by Django 3.2.2 on 2021-06-12 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_doctor_secretary'),
        ('bills', '0008_remove_bill_consultation'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='secretary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='patients.secretary'),
        ),
    ]
