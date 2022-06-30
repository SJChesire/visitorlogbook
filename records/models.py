from django.db import models

# Create your models here.
from django.db.models import Model


class Visitee(models.Model):
    visitee_name = models.CharField (max_length=60)
    visitee_status = models.CharField(max_length = 4)
    visitor_name = models.CharField(max_length= 60)



    def __str__(self):
        return self.visitee_name


class Organization(models.Model):
    organization_name = models.CharField(max_length=60)
    mobile_number = models.IntegerField()


    def __str__(self):
        return self.organization_name


class Visitor(models.Model):
    visitor_name = models.CharField (max_length = 60)
    visitee = models.ForeignKey(Visitee, on_delete=models.CASCADE,null=True,blank=True)
    organization = models.ForeignKey (Organization, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12)
    id_or_passport = models.CharField (max_length = 20)
    time_in = models.TimeField()
    time_out = models.TimeField()


    def __str__(self):
        return self.id_or_passport


