from django.contrib import admin
from .models import Record, Country, City, Person, Client, Project, Sample

admin.site.register(Record)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Person)
admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Sample)


# Register your models here.
