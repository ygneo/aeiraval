from django.contrib import admin
from aeiraval_app.models import Family, Person, Contact, Service


class FamilyAdmin(admin.ModelAdmin):
    list_display = ("created_on", "user")
    
admin.site.register(Family, FamilyAdmin)
admin.site.register(Person)
admin.site.register(Contact)
admin.site.register(Service)
