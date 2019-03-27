from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
import json
from .models import Charity
# Create your views here.
from django.http import Http404

def all_Charities(request):
    charities = Charity.objects.all()
    data = {}
    for charity in charities:
        data[charity.id] = charity.name
    return JsonResponse( data)

def charity_detail(request, charity_id):
    try:
        charity = Charity.objects.get(pk=charity_id)
    except Charity.DoesNotExist:
        raise Http404("Charity does not exist")
    data = {}
    data["name"] = charity.name
    data["addressLine1"] = charity.address_line_1
    data["addressLine2"] = charity.address_line_2
    data["postCode"] = charity.post_code
    data["charityNumber"] = charity.charity_number
    data["active"] = charity.active
    data["dateAdded"] = charity.date_added
    data["contactNumber"] = charity.contact_number

    return JsonResponse(data)