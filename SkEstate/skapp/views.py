import json
import requests
from .credentials import MpesaAccessToken, LipanaMpesaPpassword
from django.http import HttpResponse
from django.shortcuts import render, redirect
from requests.auth import HTTPBasicAuth
from skapp.models import Contact, House_detail,Booking,Agent
from skapp.forms import ContactForm,BookingForm, ImageUploadForm
from skapp.models import User, ImageModel

# Create your views here.
def home(request):
    if request.method == 'POST':
        if User.objects.filter(
                username=request.POST['username'],
                password=request.POST['password']
        ).exists():
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')

def booking(request):
     if request.method == 'POST':
                mybookings = Booking(
                    name=request.POST['name'],
                    email=request.POST['email'],
                    phone=request.POST['phone'],
                    date=request.POST['date'],
                    offer=request.POST['offer'],
                    agent=request.POST['agent'],
                    message=request.POST['message'],
                )
                mybookings.save()
                return redirect('/booking')
     else:
                return render(request, 'booking.html')

def show(request):
     allbookings = Booking.objects.all()
     return render(request, 'show.html', {'booking': allbookings})



def change(request, id):
     changebooking = Booking.objects.get(id=id)
     return render(request, 'update.html', {'booking':changebooking})


def eliminate(request, id):
    book = Booking.objects.get(id=id)
    book.delete()

    return redirect('/show')


def modify(request, id):
    modifybooking = Booking.objects.get(id=id)
    form = BookingForm(request.POST, instance=modifybooking)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request, 'update.html')

def services(request):
    return render(request, 'services.html')

def about(request):
        return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        contact_us = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        contact_us.save()
        return redirect('/contact')

    else:
        return render(request, 'contact.html')

def detail(request):
    contact_us=Contact.objects.all()
    return render(request, 'detail.html',{'contact':contact_us})


def delete(request, id):
        contact = Contact.objects.get(id=id)
        contact.delete()

        return redirect('/detail')

def edit(request, id):
    editcontact = Contact.objects.get(id=id)
    return render(request, 'edit.html', {'contact': editcontact})

def update(request, id):
    updatecontact = Contact.objects.get(id=id)
    form = ContactForm(request.POST, instance=updatecontact)
    if form.is_valid():
        form.save()
        return redirect('/detail')
    else:
        return render(request, 'edit.html')


def properties(request):
    return render(request, 'properties.html')


def starter(request):
    return render(request, 'starter.html')

def agents(request):
    return render(request, 'agents.html')


def testimonials(request):
    return render(request, 'testimonials.html')

def details(request):
    return render(request, 'service-details.html')

def single(request):
    return render(request, 'property-single.html')



def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        members = User(
            name=request.POST['name'],
            username=request.POST['username'],
            password=request.POST['password'],
        )
        members.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')

def edit(request ,id):
    editcontact = Contact.objects.get(id=id)
    form = ContactForm(request.POST, instance=editcontact)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
      return render(request, 'edit.html')


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})


def token(request):
    consumer_key = 'fUF9jNAvSXV12VjR4aNbIDq2M9miStfgRO0mdVZbMbql9hF0'
    consumer_secret = 'e8NFzxpAf0pQ0rBrW1MAlxqTGtlFEg5bG8A78m9jAOZHUEPbAbWnWX2pzvh4AaSG'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')

#MPESA API VIEWS

def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "SkTech",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")

