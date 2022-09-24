from django.contrib import admin
from .models import Departement, Employee, Attendance, Service, Client, Contract, FollowContractServices, Alert, Notification

class DepartementAdmin(admin.ModelAdmin):
    list_display = ('name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('eNum', 'name', 'departement','jobTitle','salaryType')

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('date','get_employees')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('employees')

    def get_employees(self, obj):
        return " - ".join([employee.name for employee in obj.employees.all()])

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id','name','typee','price','priceType','supervisor','fixedDeliveryDate','fixedPriceCollectDate')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id','name','phone','addressArea','created_at')

class ContractAdmin(admin.ModelAdmin):
    list_display = ('id','client','get_services','serialNum','created_at')
    # optimizing the query for each service
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('services')

    def get_services(self, obj):
        return " - ".join([service.name for service in obj.services.all()])


class FollowContractServicesAdmin(admin.ModelAdmin):
    list_display = ('client','service','startingDate','collcetStatus','remain_amount','created_by', 'created_at_date')

class AlertAdmin(admin.ModelAdmin):
    list_display = ('title','alert_date','statue','viewed_Date', 'created_at')

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title','Notification_date','created_for','statue', 'created_at')


# Register your models here.
admin.site.register(Departement, DepartementAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(FollowContractServices, FollowContractServicesAdmin)
admin.site.register(Alert, AlertAdmin)
admin.site.register(Notification, NotificationAdmin)




    # def get_services(self, obj):
    #     return str("\n".join([str(p.services) for p in obj.services.all()]))

    # def get_services(self, obj):
        # services = [p.services for p in obj.services.all()]
    #     services_names = [n.name for n in services]
        # return " "+"\n".join([str(a.services) for a in obj.services.all()])
