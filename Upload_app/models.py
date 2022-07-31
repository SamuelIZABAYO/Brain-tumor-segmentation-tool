from django.db import models
from django.contrib.auth import get_user_model


class Hospital(models.Model):
    hospital_name = models.CharField(max_length=20)
    hospital_address = models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=20)

User=get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User,related_name="doctor", on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL,null=True)
    
class Patient(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=20)
    
class PatientScan(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL,null=True)
    doctor = models.ForeignKey(Profile, on_delete=models.SET_NULL,null=True)
    original_image = models.ImageField(upload_to="Original_images/")
    result_image = models.ImageField(upload_to="Result_images/",null=True)
    created_on = models.DateTimeField(auto_now=True)
    
class PatientReport(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL,null=True)
    doctor = models.ForeignKey(Profile, on_delete=models.SET_NULL,null=True)
    created_on = models.DateTimeField(auto_now=True)
    doctor_comment = models.TextField()