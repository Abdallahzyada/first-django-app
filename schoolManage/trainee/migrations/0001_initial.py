# Generated by Django 4.2.6 on 2023-10-15 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('bdate', models.DateField()),
                ('track', models.ForeignKey(db_column='track_id', on_delete=django.db.models.deletion.CASCADE, to='tracks.track')),
            ],
        ),
    ]
