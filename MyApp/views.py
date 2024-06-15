from django.shortcuts import render,HttpResponse,redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request,"index.html")
def enquiryForm(request):
    form = EnquiryDetailsForm(request.POST or None)
    
    return render(request, "enquiry.html",{"forms":form})

def courier_list(request):
    if request.POST:
        source_pincode = request.POST.get('source_area')
        destination_pincode = request.POST.get('destination_area')
        srvType = request.POST.get('serviceType')
        shipmentType = request.POST.get('shipmentType')
        courierTransp = request.POST.get('TravelBy')
        weight = int(request.POST.get('courierWght'))
        srv_data = ServiceType.objects.get(id = int(srvType))
        shp_data = ShipmentType.objects.get(id=int(shipmentType))
        trans_data = TravelBy.objects.get(id=int(courierTransp))
        data = CostTable.objects.filter(
            serviceType=srvType,
            travelBy=courierTransp,
            shipmentType=shipmentType,
            from_weight_per_gram__lte = weight,  # Less than or equal to the weight
            to_weight_per_gram__gte = weight 
        )
        source = ServiceArea.objects.filter(id=int(source_pincode)).last()
        destination = ServiceArea.objects.filter(id=int(destination_pincode)).last()
        for  i in data : 
            if source_pincode == destination_pincode:
                price = i.localRate
            elif source.state == destination.state and source.city == destination.city:
                price = i.cityRate
            elif source.state == destination.state and source.city != destination.city:
                price = i.stateRate
            else:
                price = i.stateRate + 50
            i.courier_cost = price

        filter_data = {
            "source" : f" {source.city} ({source.state})",
            "destination" : f" {destination.city} ({destination.state})",
            "weight" : f"{weight} Gram",
            "srvType" : srv_data.typeName,
            "shipmentType": shp_data.typeName,
            "transp": trans_data.source
        }

        return render(request, 'compareList.html', {'data': data,"filterData":filter_data})
    else:
        return redirect("enquiry_form")


