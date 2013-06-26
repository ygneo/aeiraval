from django.contrib import admin
from aeiraval_app.models import Family, Person, Contact, Service, Attendance, Group, Document


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("date", "person", "reportedType")
    list_filter = ("date",)
    

class FamilyAdmin(admin.ModelAdmin):
    list_display = ("created_on", "user")
    
admin.site.register(Family, FamilyAdmin)
admin.site.register(Person)
admin.site.register(Contact)
admin.site.register(Service)
admin.site.register(Group)
admin.site.register(Document)
admin.site.register(Attendance, AttendanceAdmin)
