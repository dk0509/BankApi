from django.db import models

# Create your models here.

class Bank(models.Model):
    bank_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)

class Branch(models.Model):
    bank = models.ForeignKey('Bank',on_delete=models.CASCADE)
    ifsc = models.CharField(max_length=50,unique=True)
    branch = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.bank.name} - {self.branch} - {self.ifsc}"