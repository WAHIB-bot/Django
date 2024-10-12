from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=50)
    c_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images/category', default="")

    def __str__(self):
        return self.name

class items(models.Model):
    name = models.CharField(max_length=50)
    i_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images/item', default="")
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name='items')

