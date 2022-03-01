from django.db import models
from shopapp.models import product

# Create your models here.
class Cart(models.Model):
    c_id=models.CharField(max_length=250,blank=True)
    date_add=models.DateField(auto_now_add=True)

    class Meta:
        db_table='Cart'
        ordering=['date_add']
    def __str__(self):
        return '{}'.format(self.c_id)


class CartItem(models.Model):
    prod=models.ForeignKey(product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        db_table='CartItem'

    def sub_total(self):
        return self.prod.price* self.quantity

    def __str__(self):
        return '{}'.format(self.prod)