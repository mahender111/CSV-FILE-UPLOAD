# Generated by Django 5.0.1 on 2024-01-04 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=50, null=True)),
                ('rate', models.CharField(blank=True, max_length=50, null=True)),
                ('item_len', models.FloatField(blank=True, null=True)),
                ('item_width', models.FloatField(blank=True, null=True)),
                ('valid_from', models.DateField(blank=True, null=True)),
                ('valid_upto', models.DateField(blank=True, null=True)),
                ('valid_yn', models.BooleanField(default=True)),
            ],
        ),
    ]
