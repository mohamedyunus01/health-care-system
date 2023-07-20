from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.db.models import Subquery
from django.http import HttpResponse
from .models import *
from .forms import *
from datetime import datetime,date  
import random  as r

# Create your views here.
def phome(request):
    obj=''
    if request.GET:
        pincode =request.GET.dict()['pincode']
        obj = PHC.objects.filter(pincode=pincode)

    return render(request, 'phome.html',{'obj':obj})

def login(request):
    if request.GET:
        phc_id=request.GET.dict()['phc_id']
        password=request.GET.dict()['password']
        if password==PHC.objects.get(phc_id=phc_id).password:
            return redirect(f'/{phc_id}/home')       
    return render(request, 'login.html')


def home(request,code):
    x=PHC.objects.get(phc_id=code)
    doc=designation.objects.get(phc_id=code,role="Dean")
    no_of_patients=admission.objects.filter(phc_id=code,discharge_time__isnull=True).count()
    return render(request, 'home.html',{'x':x,'code':code,'doc':doc,'no_of_patients':no_of_patients})

def admission_details(request):
   return render(request, 'admission_details.html')





def add_doctor(request):
   return render(request, 'add_doctor.html')

def phc_details(request, code):
    obj= PHC.objects.get(phc_id=code)
    doctor=designation.objects.filter(phc_id=code)
    return render(request, 'phc_details.html',{'obj':obj,'doctor':doctor})


def Admission(request,code):
    if request.method == 'POST':
        form = AdmissionForm(request.POST, request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            admission_no=code[3:] + str(date.today()).replace('-','') + str(r.randint(100,999))
            obj.admission_no=admission_no
            obj.phc_id=PHC(phc_id=code)
            obj.save()
            #return HttpResponse(f'<center>Admission entered<br>Admission no.:{admission_no}</center>')
            return render(request, 'admission_registered.html',{'form':form,'code':code})
    else:
        form = AdmissionForm()
    return render(request, 'admission.html',{'form':form,'code':code})

def admission_details(request,code):
    obj=admission.objects.filter(phc_id=code, discharge_time__isnull=True)
    return render(request, 'admission_details.html',{'obj':obj,'code':code})


def discharge(request,code):
    if request.method == 'POST':
        form = DischargeForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            print(form.cleaned_data['admission_no'])
            obj=admission.objects.get(admission_no=form.cleaned_data['admission_no'])
            obj.discharge_status=form.cleaned_data['discharge_status']
            #obj.report=form.cleaned_data['report']
            obj.discharge_time=datetime.now()
            obj.save()

            #return HttpResponse('<center>discharged successfully</center>')
            return render(request, 'view_details.html',{'form':form,'code':code})
    else:
        form = DischargeForm()
    return render(request, 'discharge.html',{'form':form,'code':code})


def discharge_details(request,code):
    obj=admission.objects.filter(phc_id=code, discharge_time__isnull=False)
    return render(request, 'discharge_details.html',{'obj':obj,'code':code})


def doctor_details(request,code):
    doctor=designation.objects.filter(phc_id=code)
    return render(request, 'doctor_details.html',{'doctor':doctor,'code':code})



def view_details(request):
    obj=''
    if request.GET:
        admission_no =request.GET.dict()['admission_no']
        obj = admission.objects.filter(admission_no=admission_no)

    return render(request, 'view_details.html',{'obj':obj})