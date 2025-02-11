# Generated by Django 5.1.5 on 2025-01-29 13:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0002_alter_month_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='month',
            name='year',
            field=models.IntegerField(default=2025),
        ),
        migrations.AlterField(
            model_name='plan',
            name='day',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)]),
        ),
    ]
