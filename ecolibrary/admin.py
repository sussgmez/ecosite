from django.contrib import admin
from .models import NationalPark, NaturalMonument

@admin.register(NaturalMonument)
class NaturalMonumentAdmin(admin.ModelAdmin):
    pass

@admin.register(NationalPark)
class NationalParkAdmin(admin.ModelAdmin):
    pass

