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
    houseNumber = models.CharField(max_length=50, verbose_name="Num.")
    floor = models.PositiveIntegerField(verbose_name="Pis")
    door = models.PositiveIntegerField(verbose_name="Porta")
    postalCode = models.PositiveIntegerField(verbose_name="Codi postal")
    city = models.CharField(max_length=255,verbose_name="Ciutat")
    telephone = models.CharField(max_length=255,verbose_name="Codi postal")
    mobilephone = models.CharField(max_length=255,verbose_name="Num telèfon")
    isParticipatingInPE = models.BooleanField(verbose_name="Participa P.E.")
    socialSecurityNumber = models.PositiveIntegerField(verbose_name="Num Seguretat Social")
    nationalIdNumber = models.PositiveIntegerField(verbose_name="DNI")
    dateOfBirth = models.DateTimeField(auto_now=False, auto_now_add=False,verbose_name="Data de naixement")
    placeOfBirth = models.CharField(max_length=100,verbose_name="Lloc de naixement")
    occupation = models.CharField(max_length=100,verbose_name="Ocupació")
    hasPR = models.BooleanField(verbose_name="PR?") #better name?
    hasPT = models.BooleanField(verbose_name="PT?") #better name?
    PERSON_TYPES_CHOICES = (
        (0, "Child"),
        (1, "Father"),
        (2, "Mother")
        )
    personType = models.IntegerField(choices=PERSON_TYPES_CHOICES)
    family = models.ForeignKey(Family)
    group = models.ForeignKey("Group")
    documents = models.ForeignKey("Document")
    notes = models.TextField()
    
    def __unicode__(self):
        return self.firstName + " " + self.lastName
        


class Contact(models.Model):
    referrer = models.CharField(max_length=200, verbose_name="Num Seguretat Social")
    phone = models.CharField(max_length=50, verbose_name="Telefon")
    email = models.EmailField(verbose_name="E-mail")
    expedient_year = models.IntegerField(verbose_name="Any entrada exped.")
    type = models.ForeignKey("Service", verbose_name="Equipament")


class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nom")


class Group(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nom")
    startDate = models.DateTimeField(verbose_name="Any d'inici")
    endDate = models.DateTimeField(verbose_name="Any de finalització")
    courseName = models.CharField(max_length=255, verbose_name="Nom del curs")
    responsibleUser = models.ForeignKey(User, verbose_name="Usuari")
    notes = models.TextField(verbose_name="Notes")


class Attendance(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Data")
    REPORT_TYPES=(("X", "Assistència"),
                  ("J", "Falta justificada"),
                  ("M", "Malaltia"),
                  ("F", "Falta sense justificar")
                  )
    reportedType =  models.CharField(choices=REPORT_TYPES, max_length=1)
    group = models.ForeignKey(Group, verbose_name="Grup") # we need to know for which group the attendance is
    reportedUser = models.ForeignKey(User, verbose_name="User") #User who registered attendance
    person = models.ForeignKey(Person, verbose_name="Nen")


class Fees(models.Model):
    dateRegistered = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name="Data registre")
    amountPaid = models.DecimalField(max_digits=16, decimal_places=2, verbose_name="Quota pagada")
    group = models.ForeignKey(Group, verbose_name="Grup")


class Document(models.Model):
    uploadDate = models.DateField(auto_now=False,auto_now_add=False, verbose_name="Upload data")
    name = models.CharField("Name of the document", max_length=255)
    service = models.ForeignKey(Service, verbose_name="Equipament")
    author = models.CharField(max_length=255, verbose_name="Autor")
    notes = models.TextField(verbose_name="Notes")
    #Frontend? mark documents as unread. Login date of user vs uploadDate? 
				
		




     
    


