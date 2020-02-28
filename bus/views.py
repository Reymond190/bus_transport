from django.http import JsonResponse, request
from django.shortcuts import render
import requests
import json
from requests import Response
from .models import Bustrans


# def bus_transport():
#
#     return None
#
#
# var2 = bus_transport()

#
# a = {}
# a['distance'] = var2['routes'][0]['legs'][0]["distance"]["text"]
# a['duration'] = (var2['routes'][0]['legs'][0]["duration"]["text"])
# a['destination'] = (var2['routes'][0]['legs'][0]['steps'][1]['transit_details']['arrival_stop']['name'])
# a['source'] = (var2['routes'][0]['legs'][0]['steps'][1]['transit_details']['departure_stop']['name'])
# a['departure_time'] = (var2['routes'][0]['legs'][0]['steps'][1]['transit_details']['departure_time']['text'])
# a['arrival_time'] = (var2['routes'][0]['legs'][0]['steps'][1]['transit_details']['arrival_time']['text'])
# a['number_of_stops'] = (var2['routes'][0]['legs'][0]['steps'][1]['transit_details']['num_stops'])
# a['bus_number'] = (var2['routes'][0]['legs'][0]['steps'][1]['transit_details']['line']['short_name'])
#
# print (a['bus_number'])
# print ("Distance:" + a['distance'])
# print ("Duration:" + a['duration'])
# print (a['number_of_stops'])
# print ("Departure Time:" + a['departure_time'])
# print ("Arrival Time:" + a['arrival_time'])
# print ("Source:" + a['source'])
# print ("Destination:" + a['destination'])

def bus(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    origin = a
    destination = b
    try:
        transporrt_url = "https://maps.googleapis.com/maps/api/directions/json?origin=" + origin + '&destination=' + destination + '&sensor=true&transit_mode=bus' + '&key=AIzaSyAdnHOSUWloxZZSbTrhLZk0ST-RBKPQfUg'
        r = requests.get(url=transporrt_url)
        x1 = r.json()
        x2 = json.dumps(x1)
        x3 = json.loads(x2)
    finally:
        print('problem')

    return JsonResponse(x3,safe=False)

def mtc(request):
    return render(request,'mtc.html')

def home(request):
    return render(request, 'bus_status.html')