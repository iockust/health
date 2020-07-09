from django.db import models
from django.utils import timezone
from django import forms
from datetime import datetime


class Patient(models.Model):
    id = models.BigIntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'patient'

# class Health(models.Model):
#     # id = models.BigIntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
#     time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
#     value = models.IntegerField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
#     intensitytime = models.DateTimeField(db_column='IntensityTime', blank=True, null=True)  # Field name made lowercase.
#     intensity = models.IntegerField(db_column='Intensity', blank=True, null=True)  # Field name made lowercase.
#     stepsminute = models.DateTimeField(db_column='StepsMinute', blank=True, null=True)  # Field name made lowercase.
#     steps = models.IntegerField(db_column='Steps', blank=True, null=True)  # Field name made lowercase.
#     sleepminute = models.DateTimeField(db_column='SleepMinute', blank=True, null=True)  # Field name made lowercase.
#     sleepvalue = models.IntegerField(db_column='SleepValue', blank=True, null=True)  # Field name made lowercase.
#     sleeplogid = models.BigIntegerField(db_column='SleepLogId', blank=True, null=True)  # Field name made lowercase.
#     metminute = models.DateTimeField(db_column='MetMinute', blank=True, null=True)  # Field name made lowercase.
#     mets = models.DateTimeField(db_column='METs', blank=True, null=True)  # Field name made lowercase.
#     calminute = models.DateTimeField(db_column='CalMinute', blank=True, null=True)  # Field name made lowercase.
#     calories = models.FloatField(db_column='Calories', blank=True, null=True)  # Field name made lowercase.

    # def __str__(self):
    #     return self.time 

class Health(models.Model):
    # patientid = models.IntegerField(primary_key=True,blank=False, null=False)
    # patientid=models.AutoField(primary_key=True) # this is a primary key, not the patientId
    # id = models.BigIntegerField(db_column='Id', blank=True, null=True)  # This is patientId column.
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
    mets = models.IntegerField(db_column='METs', blank=True, null=True)  # Field name made lowercase.
    calminute = models.DateTimeField(db_column='CalMinute', blank=True, null=True)  # Field name made lowercase.
    calories = models.FloatField(db_column='Calories', blank=True, null=True)  # Field name made lowercase.


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

            result_list.sort(key=lambda x: x.Hour, reverse=False)
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


class WeeklyHealthSummaryManager(models.Manager):
    def weeklyHealthSummary_average(self, pid, startdate, enddate):
        from django.db import connection
        with connection.cursor() as cursor:

            cursor.execute(""" SELECT avg(value) HeartRate, AVG(Intensity) Intensity,AVG(SleepValue) AS Sleep
            ,AVG(SleepValue),Min(value) as MinHeartReate,Max(value) as MaxHearRate
            FROM `dashborad_health`  where Id=%s and (Time BETWEEN %s AND %s ) """, (pid, startdate, enddate))
            result_list = []
            for row in cursor.fetchall():
                p = self.model(AverageHeartRate=row[0], AverageIntensity=row[1],
                               AverageSleep=row[2], MinSleep=row[3], MaxSleep=row[4], MaxHearRate=row[5])
                result_list.append(p)
        return result_list


class WeeklyHealthSummary(models.Model):
    AverageHeartRate=models.IntegerField()
    AverageIntensity= models.IntegerField()
    AverageSleep= models.IntegerField()
    MinSleep= models.IntegerField()
    MaxSleep= models.IntegerField()
    MaxHearRate= models.IntegerField()

    objects=WeeklyHealthSummaryManager()

    

# SELECT avg(value) HeartRate, AVG(Intensity) Intensity,AVG(SleepMinute) Sleep,AVG(SleepMinute),Min(value) as MinHeartReate,Max(value) as MaxHearRate
#             FROM `dashborad_health`
# SELECT avg(value) HeartRate, AVG(Intensity) Intensity,AVG(SleepMinute) AS Sleep,AVG(SleepMinute),Min(value) as MinHeartReate,Max(value) as MaxHearRate
# FROM `dashborad_health`  where (Time BETWEEN '2016-04-12'AND '2016-05-12')
#  MET minute is the amount of energy expended during a minute 
# MET DescriptionThe metabolic equivalent of task is the objective measure of the ratio of the rate at which a person expends energy, relative to the mass of that person,

