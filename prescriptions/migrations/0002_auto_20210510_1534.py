# Generated by Django 3.2 on 2021-05-10 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_doctor_secretary'),
        ('prescriptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patients.doctor'),
        ),
        migrations.AddField(
            model_name='prescription',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patients.patient'),
        ),
        migrations.AddField(
            model_name='prescription',
            name='secretary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patients.secretary'),
        ),
    ]