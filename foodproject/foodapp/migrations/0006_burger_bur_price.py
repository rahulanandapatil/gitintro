# Generated by Django 4.1.2 on 2023-01-03 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0005_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='burger',
            name='bur_price',
            field=models.CharField(default='', max_length=50),
        ),
    ]