from django.urls import path
from MyApp import views as v

urlpatterns = [
    path('', v.index),
    path("enquiry/form/",v.enquiryForm,name="enquiry_form"),
    path("compare/price/",v.courier_list,name="compareCourierPrice")
]
