# Generated by Django 3.2.2 on 2021-06-08 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescriptions', '0005_auto_20210606_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='drugs_count',
            field=models.IntegerField(null=True),
        ),
    ]
