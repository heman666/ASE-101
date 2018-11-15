from django.conf.urls import url,include
from . import views

app_name = "checking_slot"

urlpatterns = [
                    url(r'^$',views.Home_page,name = 'Home'),
                    url(r'^slot$',views.Booking,name = 'Book'),
]
