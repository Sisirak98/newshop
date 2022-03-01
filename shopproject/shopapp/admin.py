from django.contrib import admin
from .models import category, product


# Register your models here.
class admincategory(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,admincategory)

class adminproduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created', 'update']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(product,adminproduct)
