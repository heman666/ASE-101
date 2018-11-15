from django import forms
from .models import Date,Slot
import datetime
from django.core import validators

global date

class Date_form(forms.ModelForm):
    class Meta:
        model = Date
        widgets = {'event_date': forms.DateInput(attrs={'class': 'datepicker'})}
        fields=('Username','Industry_name','Num_visiting','event_date')

    def clean(self):
        all_clean_data = super().clean()
        date_format_1 = "%Y-%m-%d"#{} %H:%M:%S+00:0"
        global date
        date = str(all_clean_data['event_date'])+","+str(all_clean_data['Username'])+","+str(all_clean_data['Industry_name'])
        val_date = all_clean_data.get('event_date')
        val_date1 = datetime.datetime.strptime(str(val_date), date_format).strftime("%Y-%m-%d")
        val_date1 = val_date1[:10]
        #all_clean_data['event_date'] = datetime.datetime.strptime(str(val_date1),date_format_1)
        num_visit = all_clean_data.get('Num_visiting')
        curr = datetime.date.today()
        a = datetime.datetime.strptime(str(val_date), date_format_1)
        b = datetime.datetime.strptime(str(curr), date_format_1)
        delta = a - b
        if delta.days < 5 :
            self.add_error('event_date',"You need to book before 5 days")
        if num_visit <= 0:
            self.add_error('Num_visiting','Please enter a positive number')

class Event_slot(forms.ModelForm):
    class Meta():
        model = Slot
        fields = ('slot_time',)

    def clean(self):
        all_clean_data = super().clean()
        slot = all_clean_data['slot_time']
        global date
        date = str(date)
        date = date.split(',')
        date_format_1 = "%Y-%m-%d"
        b = datetime.datetime.strptime(str(date[0]), date_format_1).strftime(date_format_1)
        result = Date.objects.get(event_date = b).Slot_set.all()
        for r in result:
            if str(slot) == str(r.slot_time):
                self.add_error('slot_time',"This slot already booked")
