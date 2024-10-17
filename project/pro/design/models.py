from django.db import models
from django.core.exceptions import ValidationError
from app.models import items
class Banner(models.Model):
    heading = models.CharField(max_length=200)
    subheading = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    bgcolor = models.TextField(blank=True, null=True)
    btntext = models.TextField(blank=True, null=True)
    btnlink = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='banners/')
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def get_solo(cls):
        banner, created = cls.objects.get_or_create(id=1) 
        return banner

    def __str__(self):
        return self.heading
    

class Banner_grid(models.Model):
    heading = models.CharField(max_length=200)
    subheading = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    bgcolor = models.TextField(blank=True, null=True)
    btntext = models.TextField(blank=True, null=True)
    btnlink = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='banners/')
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if Banner_grid.objects.count() >= 4 and not self.pk:
            # If there are already 4 records and we're creating a new one
            raise ValidationError("You can only add up to 4 BannerGrid records.")
        super(Banner_grid, self).save(*args, **kwargs)

    def __str__(self):
        return self.heading
    

class Slider(models.Model):
    heading = models.CharField(max_length=200)
    subheading = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    bgcolor = models.TextField(blank=True, null=True)
    btntext = models.TextField(blank=True, null=True)
    btnlink = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='banners/')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading
    
class featured_prod(models.Model):
    heading = models.CharField(max_length=200)
    item = models.ForeignKey(items, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.heading