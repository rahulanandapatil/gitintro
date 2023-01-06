# Generated by Django 4.1.2 on 2022-11-08 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('mess_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=300)),
                ('food', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=400)),
            ],
        ),
    ]
