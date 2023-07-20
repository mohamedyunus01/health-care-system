

from django.urls import path
from .views import *


urlpatterns = [
path('',phome),
path('login/',login),
path('<str:code>/home',home),
path('admission_details/',admission_details),
path('<str:code>/discharge',discharge),

path('add_doctor/',add_doctor),
path('details/<str:code>/',phc_details),
path('<str:code>/admission',Admission),
path('<str:code>/admission_details',admission_details),

path('<str:code>/discharge_details',discharge_details),
path('<str:code>/doctor_details',doctor_details),
path('view_details',view_details),
]