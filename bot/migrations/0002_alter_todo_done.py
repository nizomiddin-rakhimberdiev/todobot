# Generated by Django 5.0.6 on 2024-06-13 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='done',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
