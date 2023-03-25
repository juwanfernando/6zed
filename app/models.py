from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    
    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
    
class Project(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    client = models.CharField(max_length=50)
    project_name = models.CharField(max_length=50)
    client_pm = models.CharField(max_length=50)
    lab_pm = models.CharField(max_length=50)
    project_number = models.CharField(max_length=50)
    po_number = models.CharField(max_length=50)
    billing_code = models.CharField(max_length=50)
    
    def __str__(self):
        return (f"{self.project_number} {self.client}")