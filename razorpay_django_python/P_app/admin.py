from django.contrib import admin
from P_app.models import *
# Register your models here.





class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','name','amount','status', 'provider_order_id', 'payment_id', 'signature_id']

admin.site.register(Order,OrderAdmin)


# username = paymentadmin
# pass = paymentadmin@123