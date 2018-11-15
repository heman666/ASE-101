from django.shortcuts import render
from checking_slot.forms import Date_form,Event_slot
from django.contrib import messages
from django.core.mail import send_mail

def Home_page(request):
    return render(request,"index.html")

def Booking(request):
    if request.method == "POST":
        date_form = Date_form(request.POST)
        Event_form = Event_slot(request.POST)

        if(date_form.is_valid() and Event_form.is_valid()):
            dform = date_form.save()
            dform.save()
            Eform = Event_form.save(commit = False)
            Eform.slot_id = dform_id
            Eform.save()
            return render(request,"index.html")
        else:
            print(date_form.errors,"\n",Event_form.errors)
    else:
        date_form = Date_form()
        Event_form = Event_slot()
    return render(request,"check_slot/booking.html",context = {'dform':date_form,'eform':Event_form})
