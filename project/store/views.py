from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from django.core import serializers as core_serializers
from .serializers import ContractSerializer, ServiceSerializer, ClientSerializer

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class get_clients_api(APIView):
    def get(self, request):
        clients = Client.objects.all()
        data =  {'clients': list(clients.values("pk","name", ""))}
        return JsonResponse(data)

def get_client_services_api(request, client_id):
    contract = get_object_or_404(Contract,client=client_id)
    contractSerial = contract.serialNum
    client = contract.client.name
    servs=contract.services.all()
    servss = [str(s.name) for s in servs]
    data =  {'contractSerial': contractSerial,'client':client, 'services':servss}
    return JsonResponse(data)
