from django.db import models

# Create your models here.

class Meal(models.Model):
    type = [('義大利麵','義大利麵'),('蛋料理','蛋料理'),('炸物與點心','炸物與點心'),('飯料理','飯料理')]
    category = models.CharField(max_length=100, choices=type)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=250, blank=True)
    image = models.ImageField(upload_to='app/image', blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    orderno = models.CharField(max_length=10, blank=True)
    cname = models.CharField(max_length=100)
    cphone = models.CharField(max_length=20)
    cmail = models.EmailField()
    content = models.TextField()
    total_price = models.PositiveIntegerField()

    def __str__(self):
        return self.orderno

class OrderMeal(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    pname = models.CharField(max_length=100)
    unitprice = models.PositiveIntegerField()
    unit = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return self.pname
