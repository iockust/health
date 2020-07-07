# Generated by Django 2.2.13 on 2020-07-07 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashborad', '0009_health_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health',
            name='calminute',
            field=models.DateTimeField(blank=True, db_column='CalMinute', null=True),
        ),
        migrations.AlterField(
            model_name='health',
            name='intensitytime',
            field=models.DateTimeField(blank=True, db_column='IntensityTime', null=True),
        ),
        migrations.AlterField(
            model_name='health',
            name='metminute',
            field=models.DateTimeField(blank=True, db_column='MetMinute', null=True),
        ),
        migrations.AlterField(
            model_name='health',
            name='mets',
            field=models.DateTimeField(blank=True, db_column='METs', null=True),
        ),
        migrations.AlterField(
            model_name='health',
            name='sleepminute',
            field=models.DateTimeField(blank=True, db_column='SleepMinute', null=True),
        ),
        migrations.AlterField(
            model_name='health',
            name='stepsminute',
            field=models.DateTimeField(blank=True, db_column='StepsMinute', null=True),
        ),
        migrations.AlterField(
            model_name='health',
            name='time',
            field=models.DateTimeField(blank=True, db_column='Time', null=True),
        ),
    ]
