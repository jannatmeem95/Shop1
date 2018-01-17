from django.contrib import admin
from . models import ID,ShopManager,Salesperson,InventoryManager,Receiptionist,Product,\
    Invoice,Manager_notification,Inv_Manager_notification# Register your models here.


admin.site.register(ShopManager)
admin.site.register(Salesperson)
admin.site.register(InventoryManager)
admin.site.register(Receiptionist)
admin.site.register(ID)
admin.site.register(Product)
admin.site.register(Invoice)
admin.site.register(Manager_notification)
admin.site.register(Inv_Manager_notification)

