# Generated by Django 4.2.7 on 2023-11-19 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_title', models.CharField(max_length=25)),
                ('holder_id', models.CharField(max_length=10)),
                ('e_date', models.DateField()),
                ('duration', models.IntegerField()),
                ('e_time', models.TimeField()),
                ('e_detail', models.TextField()),
                ('e_complete', models.BooleanField(default=False)),
                ('capacity', models.IntegerField(default=50)),
                ('place', models.CharField(max_length=10)),
                ('cat_indoor', models.BooleanField()),
                ('cat_category', models.CharField(choices=[('Career', 'Career'), ('Social', 'Social'), ('Sport', 'Sport'), ('Panel', 'Panel')], default='Career', max_length=10)),
            ],
        ),
    ]
