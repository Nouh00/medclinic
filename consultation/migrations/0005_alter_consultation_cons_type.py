# Generated by Django 3.2.2 on 2021-06-09 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0004_alter_consultation_cons_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='cons_type',
            field=models.CharField(choices=[('urgent', 'urgent'), ('normal', 'normal')], max_length=50),
        ),
    ]