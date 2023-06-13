from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import *
from django.http import JsonResponse
import json

# Create your views here.

@csrf_exempt
def registration(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        user  = authenticate(username=username, password=password)

        if user is None:
            print("New user created")
            password2 = req.POST.get('password2')
            if password == password2:
                user = User.objects.create_user(username=username, password=password)
                userinfo = UserInfo.objects.create(user=user)
                name = req.POST.get('name')
                email = req.POST.get('email')
                contact = req.POST.get('contact')
                userinfo.name = name
                userinfo.email = email
                userinfo.contact = contact
                try:
                    userinfo.save()
                    user.save()
                except:
                    return HttpResponse("Error occured.")

                return HttpResponse("Successfully created user")
        else:
            print("User alraedy exist")
        
    return render(req, 'registration.html')


# get --> Return: {Name, Contact} json
# post --> contact, id --> Return: httpresponse
@csrf_exempt
def addcard(req):
    if req.method == 'POST':
        contact = req.POST.get('contact')
        id = req.POST.get('id')

        user = UserInfo.objects.get(contact = contact)
        user.cardid = id
        user.save()
        return HttpResponse("Card added successfully")
    else:
        print('Get method called')
        users = UserInfo.objects.filter(cardid = None)
        # Extract specific fields from each object
        data = []
        for user in users:
            fields = {
                'name': user.name,
                'contact': user.contact,
                # Add more fields as needed
            }
            data.append(fields)
        return JsonResponse(data, safe=False)
    


@csrf_exempt
def tripping(req):
    if req.method == 'GET':
        id = req.GET.get('id')
        user = UserInfo.objects.get(cardid = id).user
        try:
            trip = Trip.objects.filter(user=user).latest('id')
            if trip.end_lat is not None:
                trip = None
        except:
            trip = None
        if trip is None:
            # Trip start
            data = {}
            data['status'] = 'start'
            data['lat'] = 0
            data['lon'] = 0
            json.dumps(data)
            return JsonResponse(data, safe=False)
        else:
            #Trip end
            data = {}
            data['status'] = 'end'
            data['lat'] = trip.start_lat
            data['lon'] = trip.start_lon
            json.dumps(data)
            return JsonResponse(data, safe=False)
    else:
        #POST method
        bus_id = req.POST.get('bus_id')
        status = req.POST.get('status')
        id = req.POST.get('id')
        lat = req.POST.get('lat')
        lon = req.POST.get('lon')
        user = UserInfo.objects.get(cardid = id)
        if status == 'start':
            newtrip = Trip.objects.create(user=user.user)
            newtrip.bus_id = bus_id
            newtrip.start_lat = lat
            newtrip.start_lon = lon
            newtrip.save()
            return HttpResponse("Successfully posted data on server")
        else:
            distance = req.POST.get('distance')
            fare = int (distance)*10
            trip = Trip.objects.filter(user=user.user).latest('id')
            bus = Bus.objects.get(bus_id=bus_id)
            trip.end_lat = lat
            trip.end_lon = lon
            trip.distance = distance
            user.balance -= fare
            bus.balance += fare
            user.save()
            trip.save()
            bus.save()

            return HttpResponse("Successfully posted data on server")
            
#Recharge
def addRecharge(req):
    if req.method == 'POST':
        contact = req.POST.get('contact')
        amount = req.POST.get('amount')
        user = UserInfo.objects.get(contact=contact)
        user.balance += int(amount)
        user.save()

        return HttpResponse("Added money successfully")
    
    return render(req, 'recharge.html')
        

@csrf_exempt
def bus_registration(req):
    if req.method == "POST":
        bus_id = req.POST.get('bus_id')
        bus_name = req.POST.get('bus_name')

        bus = Bus.objects.create(bus_id = bus_id)
        bus.bus_name = bus_name
        bus.save()
        
        return HttpResponse("Bus account created successfully")
    else:
        return HttpResponse("Get method called")
        



