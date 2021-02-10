from django.db import models

# Create your models here.

class saidatech_admin_profile(models.Model):
     saidatech_admin_id=models.UUIDField( primary_key = True, editable = False)
     fname=models.CharField(max_length=100)
     lname=models.CharField(max_length=100)
     email=models.CharField(max_length=100)
     phone=models.CharField(max_length=100)
     class Meta:
         db_table='saidatech_admin'