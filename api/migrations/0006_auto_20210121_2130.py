# Generated by Django 3.1.4 on 2021-01-21 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210110_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voting',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='voting',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
