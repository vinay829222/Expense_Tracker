from django.db import models 
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class CurrentBalance(models.Model):
    current_balance=models.FloatField(default=0)

    def __str__(self):
        return f"Current Balance is {self.current_balance}."
    


class TrackingHistory(models.Model):
    current_balance=models.ForeignKey(CurrentBalance ,on_delete=models.CASCADE)
    amount=models.FloatField()
    expence_type=models.CharField(choices=(('DEBIT','DEBIT'),('CREDIT','CREDIT')),max_length=200)
    description=models.CharField(max_length=200)
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"The amount is {self.amount} for {self.description} expense type is {self.expence_type}."
    

class RequestLogs(models.Model):
    request_info=models.TextField()
    request_type=models.CharField(max_length=200)
    request_method=models.CharField(max_length=100)
    
    created_at=models.DateTimeField(auto_now_add=True)
