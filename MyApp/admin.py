from django.contrib import admin
from .models import TravelBy, ShipmentType, Courier, ServiceArea, CostTable, ServiceType
from .forms import TravelByForm, ShipmentTypeForm, CourierForm, ServiceAreaForm, CostTableForm, ServiceTypeForm


@admin.register(TravelBy)
class TravelByAdmin(admin.ModelAdmin):
    form = TravelByForm

@admin.register(ShipmentType)
class ShipmentTypeAdmin(admin.ModelAdmin):
    form = ShipmentTypeForm

@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    form = ServiceTypeForm

# @admin.register(Courier)
# class CourierAdmin(admin.ModelAdmin):
#     form = CourierForm
class CourierAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_image', 'branch', 'serviceArea']

    def display_image(self, obj):
        return obj.image.url if obj.image else None
    display_image.short_description = 'Image'

admin.site.register(Courier, CourierAdmin)

@admin.register(ServiceArea)
class ServiceAreaAdmin(admin.ModelAdmin):
    form = ServiceAreaForm

@admin.register(CostTable)
class CostTableAdmin(admin.ModelAdmin):
    form = CostTableForm
    fields = ["courier","serviceType","shipmentType","travelBy","from_weight_per_gram","to_weight_per_gram","localRate","cityRate","stateRate"]
    # list_display = [field.name for field in CostTable._meta.get_fields()]
    list_display =["courier","serviceType","shipmentType","travelBy","from_weight_per_gram","to_weight_per_gram","localRate","cityRate","stateRate"]
