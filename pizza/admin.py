from django.contrib import admin

from .models import  Pizza,Extra,Order,Sub,Addition,Pastasalad,Dinner
# Register your models here.
admin.site.register(Pizza)
admin.site.register(Extra)
admin.site.register(Order)
admin.site.register(Sub)
admin.site.register(Addition)
admin.site.register(Pastasalad)
admin.site.register(Dinner)

