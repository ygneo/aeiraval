# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Family(models.Model):
    created_on = models.DateField(auto_now_add=True,
                                  null=False, blank=False,
                                  verbose_name="Data")
    name = models.CharField(max_length=255, verbose_name="Nom")
    user = models.ForeignKey(User, verbose_name="usuari")
    STATUS_CHOICES = (
        (0, "Matrimoni"),
        (1, "Separ. / Divorci"),
        (2, "Viudetat"),
        (3, "Monoparental"),
        (4, "Altres")
        )
    status = models.IntegerField(choices=STATUS_CHOICES, verbose_name="Estat civil")
    father = models.ForeignKey("Person", null=True, blank=True, related_name="father", verbose_name="Pare")
    mother = models.ForeignKey("Person", null=True, blank=True, related_name="mother", verbose_name="Mare")
    genogram = models.TextField(verbose_name="Genogram familiar")

    class Meta:
        verbose_name = "Família"
        verbose_name_plural = "Famílies"


class Person(models.Model):
    firstName = models.CharField(max_length=255, verbose_name="Nom")
    lastName = models.CharField(max_length=255, verbose_name="Cognom")
    address = models.CharField(max_length=255, verbose_name="Adreça")
    houseNumber = models.CharField(max_length=50, verbose_name="Num."))
    floor = models.PositiveIntegerField(verbose_name="Pis")
    door = models.PositiveIntegerField(verbose_name="Porta")
    postalCode = models.PositiveIntegerField()
    city = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    mobilephone = models.CharField(max_length=255)
    isParticipatingInPE = models.BooleanField()
    socialSecurityNumber = models.PositiveIntegerField()
    nationalIdNumber = models.PositiveIntegerField()
    dateOfBirth = models.DateTimeField(auto_now=False, auto_now_add=False)
    placeOfBirth = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    hasPR = models.BooleanField() #better name?
    hasPT = models.BooleanField() #better name?
    PERSON_TYPES_CHOICES = (
        (0, "Child"),
        (1, "Father"),
        (2, "Mother")
        )
    personType = models.IntegerField(choices=PERSON_TYPES_CHOICES)
    family = models.ForeignKey(Family)
    group = models.ForeignKey("Group")
    attendance = models.ForeignKey("Attendance")
    documents = models.ForeignKey("Document")
    notes = models.TextField()        


class Contact(models.Model):
    referrer = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    expedient_year = models.IntegerField()
    type = models.ForeignKey("Service")


class Service(models.Model):
    name = models.CharField(max_length=200)


class Group(models.Model):
    name = models.CharField(max_length=255)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    courseName = models.CharField(max_length=255)
    responsibleUser = models.ForeignKey(User)
    notes = models.TextField()


class Attendance(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    REPORT_TYPES=((0, "Attended"),
                  (1, "Justified absence"),
                  (2, "Illness"),
                  (3, "Unjustified absence")
                  )
    reportedType =  models.IntegerField(choices=REPORT_TYPES)
    group = models.ForeignKey(Group) # we need to know for which group the attendance is
    reportedUser = models.ForeignKey(User) #User who registered attendance


class Fees(models.Model):
    dateRegistered = models.DateTimeField(auto_now=False, auto_now_add=False)
    amountPaid = models.DecimalField(max_digits=16, decimal_places=2)
    group = models.ForeignKey(Group)


class Document(models.Model):
    uploadDate = models.DateField(auto_now=False,auto_now_add=False)
    name = models.CharField("Name of the document", max_length=255)
    service = models.ForeignKey(Service)
    author = models.CharField(max_length=255)
    notes = models.TextField()
    #Frontend? mark documents as unread. Login date of user vs uploadDate? 
				
		




     
    


