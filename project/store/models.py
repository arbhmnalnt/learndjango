import datetime
from django.utils.timezone import now

from django.db import models

# Create your models here.
class TimeStampMixin(models.Model):
    created_at      = models.DateTimeField(auto_now_add=True,null=True)
    created_at_date = models.DateField(auto_now_add=True,null=True)
    updated_at      = models.DateTimeField(auto_now=True,null=True)
    updated_at_date = models.DateField(auto_now=True,null=True)

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
        elif hasattr(self, 'title'):
            return str(self.title)
        elif hasattr(self, 'COLLECT_STATUS'):
            return str(self.service)





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
    eNum         = models.IntegerField(null=True, blank=True, unique=True, db_index=True, verbose_name="الرقم التعريفى") # custom employee number for future us as like his id in company or any use else
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
    fixedPriceCollectDate_more    = models.DateField(null=True, blank=True) # may neeed in future use
    notes                    = models.TextField(max_length=50,null=True, blank=True)

class Client(TimeStampMixin,models.Model):
    name            = models.CharField(max_length=50,null=True, blank=True)
    phone           = models.CharField(max_length=11, null=True, blank=True)
    addressArea     = models.CharField(max_length=50,null=True, blank=True)
    addressBuilding = models.CharField(max_length=50,null=True, blank=True, help_text="تفاصيل العمارة السكنية")
    addressApartment= models.CharField(max_length=50,null=True, blank=True, help_text="تفاصيل الشقه")
    addressDetails  = models.CharField(max_length=50,null=True, blank=True, help_text="اى تفاصيل إخرى للعنوان")
    CNum            = models.IntegerField(null=True, blank=True, unique=True, db_index=True, verbose_name="الرقم التعريفى") # custom client number for future us as like his id in company or any use else
    notes           = models.TextField(max_length=50,null=True, blank=True)

class Contract(TimeStampMixin,models.Model):
    serialNum       = models.IntegerField(help_text="رقم سريال متفرد لكل تعاقد",unique=True,null=True, blank=True,db_index=True)
    client          = models.ForeignKey('Client', related_name='contract_client', on_delete=models.CASCADE,null=True, blank=True)
    services        = models.ManyToManyField('Service',related_name='services')
    created_by      = models.ForeignKey('Employee', related_name='created_by_employee', on_delete=models.CASCADE,null=True, blank=True)
    modified_by     = models.ForeignKey('Employee', on_delete=models.CASCADE,null=True, blank=True)
    notes           = models.TextField(max_length=50,null=True, blank=True)

class FollowContractServices(TimeStampMixin,models.Model):
    PAID = 'تم الدفع'
    PAYMENT_REQUIRED = 'مطلوب الدفع'
    COLLECTING_DATE = 'فى انتظار ميعاد التحصيل'  # Waiting for collection date
    COLLECT_STATUS= [
        (PAID, 'Service has been paid already'),
        (PAYMENT_REQUIRED, 'Payment required for the service'),
        (COLLECTING_DATE, 'Waiting for collection date'),
    ]
    #
    PAID_NUM = 1
    PAYMENT_REQUIRED_NUM = 2
    COLLECTING_DATE_NUM = 3
    COLLECT_STATUS_NUM = (
        (PAID_NUM, 'Service has been paid already'),
        (PAYMENT_REQUIRED_NUM, 'Payment required for the service'),
        (COLLECTING_DATE_NUM, 'Waiting for collection date'),
    )
    #
    client               = models.ForeignKey('Client', related_name='client', on_delete=models.CASCADE,null=True, blank=True)
    service              = models.ForeignKey('Service', related_name='service', on_delete=models.CASCADE,null=True, blank=True)
    startingDate         = models.DateField(null=True, blank=True)
    serviceDueDate         = models.DateField(null=True, blank=True, verbose_name="تاريخ اداء الخدمه")
    collcetStatus        = models.CharField(max_length=50,null=True, blank=True, choices=COLLECT_STATUS, default=COLLECTING_DATE)
    collcetStatusNums    = models.IntegerField(null=True, blank=True, choices=COLLECT_STATUS_NUM, default=COLLECTING_DATE_NUM,db_index=True)
    total_amount         = models.IntegerField(null=True, blank=True, verbose_name="المبلغ المطلوب تحصيله")
    collected_amount     = models.IntegerField(null=True, blank=True, verbose_name="المبلغ الذى تم تحصيله")
    remain_amount        = models.IntegerField(null=True, blank=True, verbose_name="المبلغ المتبقى")
    created_by           = models.ForeignKey('Employee', related_name='employee', on_delete=models.CASCADE,null=True, blank=True)
    modified_by          = models.ForeignKey('Employee', on_delete=models.CASCADE,null=True, blank=True)

class Alert(TimeStampMixin,models.Model):
    OPEN = 1
    CLOSED = 2
    ALERT_STATUE = (
        (OPEN, 'Alert has not been viewed'),
        (CLOSED, 'Alert is viewed already by the employee'),
    )
    title           = models.CharField(max_length=50,null=True, blank=True)
    content         = models.CharField(max_length=200,null=True, blank=True, verbose_name="محتوى التنبيه")
    alert_date      = models.DateField(null=True, blank=True, verbose_name="تاريخ التنبيه")
    created_for     = models.ForeignKey('Employee', related_name='alert_employee_rquired', on_delete=models.CASCADE,null=True, blank=True, verbose_name="تنبيه موج للموظف")
    viewed_by       = models.ForeignKey('Employee', related_name='alert_employee_viewed', on_delete=models.CASCADE,null=True, blank=True, verbose_name="تم اغلاق التنبه بواسطة ")
    viewed_Date     = models.DateField(null=True, blank=True)
    statue          = models.IntegerField(null=True, blank=True, choices=ALERT_STATUE, default=OPEN,db_index=True)

class Notification(TimeStampMixin,models.Model):
    OPEN = 1
    CLOSED = 2
    NOTIFICATION_STATUE = (
        (OPEN, 'Alert has not been viewed'),
        (CLOSED, 'Alert is viewed already by the employee'),
    )
    title                  = models.CharField(max_length=50,null=True, blank=True)
    content                = models.CharField(max_length=200,null=True, blank=True, verbose_name="محتوى الاشعار")
    Notification_date      = models.DateField(null=True, blank=True)
    created_for            = models.ForeignKey('Employee', related_name='note_employee_rquired', on_delete=models.CASCADE,null=True, blank=True, verbose_name="اشعار موجه لـــ")
    viewed_by              = models.ForeignKey('Employee', related_name='note_employee_viewed', on_delete=models.CASCADE,null=True, blank=True, verbose_name="تم اغلاق الاشعار بواسطة ")
    viewed_Date            = models.DateField(null=True, blank=True)
    statue                 = models.IntegerField(null=True, blank=True, choices=NOTIFICATION_STATUE, default=OPEN,db_index=True)
