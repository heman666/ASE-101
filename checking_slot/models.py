from django.db import models
from django.core import validators
from django.forms import ValidationError
from datetime import datetime
from django.conf import settings


class Date(models.Model):
    Username = models.CharField(max_length = 100)
    Industry_name = models.CharField(max_length = 50)
    Num_visiting = models.IntegerField(default = 1)
    event_date = models.DateField(default = datetime.today())

    def __str__(self):
        return '{} {} {}'.format(self.Username,self.Industry_name,self.event_date)

timings = (('1','9:30'),('2','11:30'),('3','14:30'))

class Slot(models.Model):
    slot_id = models.ForeignKey(Date,on_delete = models.CASCADE)
    slot_time = models.CharField(max_length =10, choices=timings,default = '9:30')
    def __str__(self):
        return '{} {}'.format(self.slot_id,self.slot_time)
