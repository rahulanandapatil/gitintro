# Generated by Django 4.1.2 on 2022-11-09 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Burger',
            fields=[
                ('bur_id', models.AutoField(primary_key=True, serialize=False)),
                ('bur_name', models.CharField(max_length=50)),
                ('bur_desc', models.CharField(max_length=500)),
            ],
        ),
    ]
