from django.contrib import admin

# Register your models here.

from .models import (
    Category,
    Product,
    Slider,
    Laptop,
    CPUCooler,
    Casing,
    GraphicsCard,
    HardDisk,
    Keyboards,
    Monitor,
    Motherboard,
    Mouse,
    PowerSupply,
    Processors,
    RAM,
    SSD,
)


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title', )}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title', )}



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Slider)
admin.site.register(Laptop)
admin.site.register(CPUCooler)
admin.site.register(Casing)
admin.site.register(GraphicsCard)
admin.site.register(HardDisk)
admin.site.register(Keyboards)
admin.site.register(Monitor)
admin.site.register(Motherboard)
admin.site.register(Mouse)
admin.site.register(PowerSupply)
admin.site.register(Processors)
admin.site.register(RAM)
admin.site.register(SSD)