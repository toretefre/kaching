# Generated by Django 2.0 on 2018-02-01 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20180201_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mifare',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]