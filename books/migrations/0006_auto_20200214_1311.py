# Generated by Django 3.0.3 on 2020-02-14 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20200214_0659'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['id'], name='id_index'),
        ),
    ]
