from django.db import models
from django.utils import timezone

# Create your models here.
class Health(models.Model):
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
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

    

