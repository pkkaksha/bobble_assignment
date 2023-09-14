# Generated by Django 4.2.5 on 2023-09-14 13:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoomTempData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.CharField(max_length=100)),
                ('temp_in_room', models.IntegerField()),
                ('changed_at', models.DateTimeField(default=datetime.datetime(2023, 9, 14, 13, 38, 14, 909290))),
            ],
        ),
    ]