# Generated by Django 2.2 on 2023-11-14 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_profile', '0009_auto_20231029_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petowner',
            name='location',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
