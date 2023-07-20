from django.db import models

# Create your models here.
class PHC(models.Model):
    phc_id = models.CharField(primary_key=True,max_length=50)
    phc_name = models.CharField(max_length=100, null=True)
    summary = models.CharField(max_length=3000, null=True)
    password = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()
    mobile = models.IntegerField()
    no_of_beds = models.IntegerField()
    gmap_link = models.CharField(max_length=1000, null=True)

class medician(models.Model):
    medician_id = models.CharField(primary_key=True,max_length=50)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.IntegerField()


class designation(models.Model):
    phc_id = models.ForeignKey(PHC, on_delete=models.CASCADE)
    medician_id = models.ForeignKey(medician, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)



class admission(models.Model):
    admission_no = models.IntegerField()
    phc_id = models.ForeignKey(PHC, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=50,null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=11,null=True)
    guardian_name = models.CharField(max_length=50,null=True)
    street = models.CharField(max_length=50,null=True)
    city = models.CharField(max_length=50,null=True)
    district = models.CharField(max_length=50,null=True)
    mobile = models.IntegerField(null=True)
    blood_group = models.CharField(max_length=4,null=True)
    cause = models.CharField(max_length=50)
    admission_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    discharge_time = models.DateTimeField(auto_now=False, auto_now_add=False,null=True)
    discharge_status = models.CharField(max_length=50)
    report = models.FileField(upload_to="pdf",null=True)


class immunisation(models.Model):
    phc_id = models.ForeignKey(PHC, on_delete=models.CASCADE)
    year = models.IntegerField()
    month = models.CharField(max_length=50)
    vaccine_name = models.CharField(max_length=50)
    no_of_vaccines = models.IntegerField()
