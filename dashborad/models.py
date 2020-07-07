from django.db import models
from django.utils import timezone
from django import forms
from datetime import datetime

# Create your models here.
class Health(models.Model):
    # input_formats
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    # time=forms.DateTimeField(input_formats=["%d %b %Y %H:%M:%S %Z"])
    # time=models.DateTimeField(auto_now=True)
    # time=models.DateTimeField(default=datetime.now())
    # models.DecimalField(max_digits=10, decimal_places=4, null=True)
    value = models.IntegerField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    intensitytime = models.TextField(db_column='IntensityTime', blank=True, null=True)  # Field name made lowercase.
    intensity = models.IntegerField(db_column='Intensity', blank=True, null=True)  # Field name made lowercase.
    stepsminute = models.TextField(db_column='StepsMinute', blank=True, null=True)  # Field name made lowercase.
    steps = models.IntegerField(db_column='Steps', blank=True, null=True)  # Field name made lowercase.
    sleepminute = models.TextField(db_column='SleepMinute', blank=True, null=True)  # Field name made lowercase.
    sleepvalue = models.IntegerField(db_column='SleepValue', blank=True, null=True)  # Field name made lowercase.
    sleeplogid = models.BigIntegerField(db_column='SleepLogId', blank=True, null=True)  # Field name made lowercase.
    metminute = models.TextField(db_column='MetMinute', blank=True, null=True)  # Field name made lowercase.
    mets = models.IntegerField(db_column='METs', blank=True, null=True)  # Field name made lowercase.
    calminute = models.TextField(db_column='CalMinute', blank=True, null=True)  # Field name made lowercase.
    calories = models.FloatField(db_column='Calories', blank=True, null=True)  # Field name made lowercase.


class Patient(models.Model):
    id = models.BigIntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patient'


<<<<<<< HEAD

class Health(models.Model):
    # id = models.BigIntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    value = models.IntegerField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    intensitytime = models.DateTimeField(db_column='IntensityTime', blank=True, null=True)  # Field name made lowercase.
    intensity = models.IntegerField(db_column='Intensity', blank=True, null=True)  # Field name made lowercase.
    stepsminute = models.DateTimeField(db_column='StepsMinute', blank=True, null=True)  # Field name made lowercase.
    steps = models.IntegerField(db_column='Steps', blank=True, null=True)  # Field name made lowercase.
    sleepminute = models.DateTimeField(db_column='SleepMinute', blank=True, null=True)  # Field name made lowercase.
    sleepvalue = models.IntegerField(db_column='SleepValue', blank=True, null=True)  # Field name made lowercase.
    sleeplogid = models.BigIntegerField(db_column='SleepLogId', blank=True, null=True)  # Field name made lowercase.
    metminute = models.DateTimeField(db_column='MetMinute', blank=True, null=True)  # Field name made lowercase.
    mets = models.DateTimeField(db_column='METs', blank=True, null=True)  # Field name made lowercase.
    calminute = models.DateTimeField(db_column='CalMinute', blank=True, null=True)  # Field name made lowercase.
    calories = models.FloatField(db_column='Calories', blank=True, null=True)  # Field name made lowercase.
=======
class HourlyHeartRateManager(models.Manager):
    def hourly_avg_rate(self, pid, startdate, enddate):
        from django.db import connection
        with connection.cursor() as cursor:

            cursor.execute("""SELECT Hour(time) Hour, avg(value) HoulryHeartRate 
            FROM `dashborad_health` 
            where Id=%s and time BETWEEN %s and %s GROUP by Hour(time)""", (pid, startdate, enddate))
            result_list = []
            for row in cursor.fetchall():
                p = self.model(Hour=row[0], HeartRate=row[1])
                result_list.append(p)
            for h in range(24):
                if not self.containsHour(result_list, lambda x: x.Hour == h):
                    p = self.model(Hour=h, HeartRate=0)
                    result_list.append(p)

        return result_list

    def containsHour(self, list, filter):
        for x in list:
            if filter(x):
                return True
        return False


class HourlyHeartRate(models.Model):
    HeartRate = models.IntegerField()
    Hour = models.IntegerField()
    objects = HourlyHeartRateManager()
>>>>>>> 816bac3b440e7e2e35e89c9fde2b9a6cd2bfcf0d
