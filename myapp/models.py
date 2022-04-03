from django.db import models

class Customer(models.Model):
  customer_id=models.AutoField(primary_key=True)
  customer_name=models.CharField(max_length=100,blank=False)
  personal_mail=models.EmailField(max_length=100,blank=False,unique=True)
  password=models.CharField(max_length=100,blank=False)

class Meta:
  db_table = "usersignup_table"