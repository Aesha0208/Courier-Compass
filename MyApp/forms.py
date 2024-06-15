from django import forms
from .models import *

class TravelByForm(forms.ModelForm):
    class Meta:
        model = TravelBy
        fields = '__all__'

class ShipmentTypeForm(forms.ModelForm):
    class Meta:
        model = ShipmentType
        fields = '__all__'

class CourierForm(forms.ModelForm):
    class Meta:
        model = Courier
        fields = '__all__'

class ServiceAreaForm(forms.ModelForm):
    class Meta:
        model = ServiceArea
        fields = '__all__'

class CostTableForm(forms.ModelForm):
    class Meta:
        model = CostTable
        fields = '__all__'

class ServiceTypeForm(forms.ModelForm):
    class Meta:
        model = ServiceType
        fields = '__all__'

class EnquiryDetailsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EnquiryDetailsForm, self).__init__(*args, **kwargs)
        self.fields['serviceType'].empty_label = None  # Corrected attribute name
        self.fields['shipmentType'].empty_label = None  # Corrected attribute name
        self.fields['source_area'].empty_label = "select by pin code ..."  # Corrected attribute name
        self.fields['destination_area'].empty_label = "select by pin code ..."  # Corrected attribute name
        self.fields['TravelBy'].empty_label = None  # Corrected attribute name
        
    class Meta:
        model = EnquiryForm
        fields = ['source_area', 'destination_area','serviceType','shipmentType', 'TravelBy', 'courierWght']
        labels = {
            'source_area': 'Source Area',
            'destination_area': 'Destination Area',
            'serviceType': 'Service Type',
            'shipmentType': 'Shipment Type',
            'TravelBy': 'Travel By',
            'courierWght': 'Courier Weight',
        }
        widgets = {
            'source_area': forms.Select(attrs={'class': 'form-control select2'}),
            'destination_area': forms.Select(attrs={'class': 'form-control select2'}),
            'serviceType': forms.Select(attrs={'class': 'form-control select2'}),
            'shipmentType': forms.Select(attrs={'class': 'form-control select2'}),
            'TravelBy': forms.Select(attrs={'class': 'form-control select2'}),
            'courierWght': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter courier weight'}),
        }
