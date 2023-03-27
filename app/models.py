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
    

class Client(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
       
    
class Project(models.Model):
    #ForeignKey(COC, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    project_number = models.CharField(max_length=50)
    project_name = models.CharField(max_length=50)
    coc_number = models.CharField(max_length=50)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    client_pm = models.CharField(max_length=50)
    lab_pm = models.CharField(max_length=50)    
    po_number = models.CharField(max_length=50)
    billing_code = models.CharField(max_length=50)
    approved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.project_number
    
    
class Sample(models.Model):    
    project_number = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    sample_id = models.CharField(max_length=50)
    sample_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.sample_id
    

class Store(models.Model):    
    sample_id = models.ForeignKey(Sample, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    fridge_number = models.CharField(max_length=50)
    rack = models.CharField(max_length=50)
    dore = models.BooleanField(default=False)
    
    def __str__(self):
        return self.sample_number
        
    
class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=124)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name