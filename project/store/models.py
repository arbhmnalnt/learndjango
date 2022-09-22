import datetime
from django.utils.timezone import now

from django.db import models

# Create your models here.
class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        abstract = True

    def __str__(self):
        if hasattr(self, 'name'):
            return self.name
        elif hasattr(self, 'image'):
            return str(self.id)

        elif hasattr(self, 'serialNum'):
            return str(self.id)

        elif hasattr(self, 'employees'):
            return f"دفتر حضور يوم :  {self.date}"




class Departement(TimeStampMixin,models.Model):
    name  = models.CharField(max_length=50)
    notes = models.TextField(max_length=50,null=True, blank=True)


class Employee(TimeStampMixin,models.Model):
    name         = models.CharField(max_length=50 , null=True, blank=True,  verbose_name="الاسم")
    address      = models.CharField(max_length=50 , null=True, blank=True)
    phone        = models.CharField(max_length=11, null=True, blank=True)
    departement  = models.ForeignKey('Departement', on_delete=models.CASCADE,  null=True, blank=True)
    jobTitle     = models.CharField(max_length=50, null=True, blank=True)
    dateOfEmployment  = models.DateField(null=True, blank=True, verbose_name="تاريخ التعيين")
    dateOfBirth  = models.DateField(null=True, blank=True)
    naId         = models.CharField(max_length=14, null=True, blank=True)
    typee        = models.CharField(max_length=50 , null=True, blank=True) # will be get front as [ employee or worker ]
    salaryType   = models.CharField(max_length=50 , null=True, blank=True) # will be get front as [ daily or monthly ]
    salary       = models.IntegerField(null=True, blank=True)
    eNum         = models.IntegerField(null=True, blank=True, unique=True, verbose_name="الرقم التعريفى") # custom employee number for future us as like his id in company or any use else
    notes        = models.TextField(max_length=50,null=True, blank=True)

class Attendance(TimeStampMixin,models.Model):
    date         = models.DateField(null=True, blank=True)
    employees     = models.ManyToManyField('Employee',related_name='employees')
    notes        = models.TextField(max_length=50,null=True, blank=True)


class Service(TimeStampMixin,models.Model):
    name                     = models.CharField(max_length=50,null=True, blank=True)
    typee                    = models.CharField(max_length=50,null=True, blank=True)
    price                    = models.IntegerField(null=True, blank=True)
    priceType                = models.CharField(max_length=50,null=True, blank=True)
    providers                = models.ManyToManyField('Employee',related_name='providers')
    supervisor               = models.ForeignKey('Employee', related_name='supervisor', on_delete=models.CASCADE,null=True, blank=True)
    fixedDeliveryDate        = models.IntegerField(default=1,null=True, blank=True) # check that the day nuumber is between 1-30 in api insert
    fixedPriceCollectDate    = models.IntegerField(default=1,null=True, blank=True) # check that the day nnumber is between 1-30 in api insert
    notes                    = models.TextField(max_length=50,null=True, blank=True)

class Client(TimeStampMixin,models.Model):
    name            = models.CharField(max_length=50,null=True, blank=True)
    phone           = models.CharField(max_length=11, null=True, blank=True)
    addressArea     = models.CharField(max_length=50,null=True, blank=True)
    addressBuilding = models.CharField(max_length=50,null=True, blank=True, help_text="تفاصيل العمارة السكنية")
    addressApartment= models.CharField(max_length=50,null=True, blank=True, help_text="تفاصيل الشقه")
    addressDetails  = models.CharField(max_length=50,null=True, blank=True, help_text="اى تفاصيل إخرى للعنوان")
    CNum            = models.IntegerField(null=True, blank=True, unique=True, verbose_name="الرقم التعريفى") # custom client number for future us as like his id in company or any use else
    notes           = models.TextField(max_length=50,null=True, blank=True)

class Contract(TimeStampMixin,models.Model):
    serialNum       = models.IntegerField(help_text="رقم سريال متفرد لكل تعاقد",unique=True,null=True, blank=True)
    client          = models.ForeignKey('Client', related_name='client', on_delete=models.CASCADE,null=True, blank=True)
    services        = models.ManyToManyField('Service',related_name='services')
    created_by      = models.ForeignKey('Employee', related_name='employee', on_delete=models.CASCADE,null=True, blank=True)
    modified_by     = models.ForeignKey('Employee', on_delete=models.CASCADE,null=True, blank=True)
    notes           = models.TextField(max_length=50,null=True, blank=True)


