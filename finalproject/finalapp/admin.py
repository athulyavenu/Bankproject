from django.contrib import admin

# Register your models here.
from . models import Person,Branch, District

admin.site.register(Person)
admin.site.register(Branch)
admin.site.register(District)
