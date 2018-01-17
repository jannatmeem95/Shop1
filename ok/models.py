from django.db import models

# Create your models here.

class ID(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=15)
    type=models.CharField(max_length=25)

#inv_number, pro_id, date, emp_id, quantity_bought, total_cost

class ShopManager(models.Model):
    manager_username = models.CharField(max_length=50)
    manager_name = models.CharField(max_length=250)

    def __str__(self):
        return self.manager_username

class InventoryManager(models.Model):
    manager_username = models.CharField(max_length=50)
    manager_name = models.CharField(max_length=250)

    def __str__(self):
        return self.manager_username


class Salesperson(models.Model):
    emp_username = models.CharField(max_length=50)
    emp_name = models.CharField(max_length=250)
    manager_id = models.ForeignKey(ShopManager, on_delete=models.CASCADE)

class Receiptionist(models.Model):
    emp_username = models.CharField(max_length=50)
    emp_name = models.CharField(max_length=250)
    manager_id = models.ForeignKey(ShopManager, on_delete=models.CASCADE)


class Product(models.Model):
    pro_name=models.CharField(max_length=250)
    price=models.CharField(max_length=250)
    color=models.CharField(max_length=100)
    pic=models.CharField(max_length=100)
    qty=models.CharField(max_length=250)

class Invoice(models.Model):
    pro_id=models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    pro_price = models.CharField(max_length=250)
    pro_qty = models.CharField(max_length=250)

class Manager_notification(models.Model):
    notification = models.CharField(max_length=250)

class Inv_Manager_notification(models.Model):
    notification = models.CharField(max_length=250)