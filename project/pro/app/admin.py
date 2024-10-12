from django.contrib import admin
from . models import category, items
# Register your models here.
@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
  list_display = ("c_id", "name")

@admin.register(items)
class categoryAdmin(admin.ModelAdmin):
  list_display = ("i_id", "name","category")
