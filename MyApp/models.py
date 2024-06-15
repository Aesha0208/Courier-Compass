from django.db import models

class ShipmentType(models.Model):
    typeName = models.CharField(max_length=100)
    def __str__(self):
        return self.typeName

class Courier(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='courier_images/')
    branch = models.CharField(max_length=100)
    serviceArea = models.ForeignKey('ServiceArea', related_name='couriers', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class ServiceType(models.Model):
    typeName = models.CharField(max_length=100)
    def __str__(self):
        return self.typeName

class ServiceArea(models.Model):
    pincode = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zone = models.CharField(max_length=100)
    def __str__(self):
            return self.pincode

class TravelBy(models.Model):
    source = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.source

class Users(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

class EnquiryForm(models.Model):
    source_area = models.ForeignKey(ServiceArea, related_name='enquiry_source',on_delete=models.CASCADE)
    destination_area = models.ForeignKey(ServiceArea,related_name='enquiry_destination',on_delete=models.CASCADE)
    courierService = models.ForeignKey('Courier', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    serviceType = models.ForeignKey('ServiceType', on_delete=models.CASCADE)
    shipmentType = models.ForeignKey('ShipmentType', on_delete=models.CASCADE)
    TravelBy = models.ForeignKey('TravelBy', on_delete=models.CASCADE,blank=False)
    courierWght = models.CharField(max_length=100,default=0)

class CostTable(models.Model):
    courier = models.ForeignKey('Courier', on_delete=models.CASCADE)
    serviceType = models.ForeignKey('ServiceType', on_delete=models.CASCADE)
    shipmentType = models.ForeignKey('ShipmentType', on_delete=models.CASCADE)
    travelBy = models.ForeignKey('TravelBy', on_delete=models.CASCADE)
    from_weight_per_gram = models.DecimalField(max_digits=10, decimal_places=2)
    to_weight_per_gram = models.DecimalField(max_digits=10, decimal_places=2)
    localRate = models.DecimalField(max_digits=10, decimal_places=2)
    cityRate = models.DecimalField(max_digits=10, decimal_places=2)
    stateRate = models.DecimalField(max_digits=10, decimal_places=2)
