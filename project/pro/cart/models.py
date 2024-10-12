from django.db import models
from app.models import items
# Create your models here.
class cartList(models.Model):
    id = models.AutoField(primary_key=True)
    item_id = models.ForeignKey(items, on_delete=models.CASCADE, related_name='items')
    