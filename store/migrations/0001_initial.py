# Generated by Django 2.0 on 2017-12-23 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('mail', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('balance', models.IntegerField(default=0)),
                ('mifare', models.PositiveIntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('manufacturer', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('EAN', models.PositiveIntegerField()),
                ('active_item', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('checked_out', models.BooleanField(verbose_name=models.BooleanField(default=False))),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Customer')),
                ('items', models.ManyToManyField(to='store.Item')),
            ],
        ),
    ]
