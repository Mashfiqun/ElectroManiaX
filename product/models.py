from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(unique=True, max_length=150)
    featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __str__(self) -> str:
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(unique=True, max_length=250)
    featured = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    thumbnail = models.URLField()
    description = models.TextField(null=True, blank=True, default='N/A')
    in_stock = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.title

    @property
    def related(self):
        return Product.objects.filter(category=self.category).exclude(pk=self.pk)
class Laptop(Product):
    processor = models.CharField(max_length=250, unique=True)
    brand = models.CharField(max_length=250, default="")
    display_size = models.DecimalField(decimal_places=1, max_digits=3)
    display_type = models.CharField(max_length=250)
    ram_size = models.CharField(max_length=250)
    ram_type = models.CharField(max_length=250)
    bus_speed = models.CharField(max_length=250)
    storage_size = models.CharField(max_length=250)
    storage_type = models.CharField(max_length=250)
    graphics_size = models.CharField(max_length=250)
    graphics_type = models.CharField(max_length=250)
    keyboard = models.CharField(max_length=250)
    camera = models.CharField(max_length=250)
    speaker = models.BooleanField(default=True)
    mic = models.BooleanField(default=True)
    wifi = models.CharField(max_length=250)
    battery = models.CharField(max_length=250)
    weight = models.CharField(max_length=250)


class Slider(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=150)
    banner = models.ImageField(upload_to='banners')
    show = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class CPUCooler(Product):
    brand = models.CharField(max_length=250, default="")
    fan_speed = models.IntegerField()
    cooler_type = models.CharField(max_length=250) 
    rgb = models.CharField(max_length=10) 
    wattage = models.IntegerField()

class Casing(Product):
    brand = models.CharField(max_length=250, default="")
    form_factor = models.CharField(max_length=250) 
    material = models.CharField(max_length=250)
    color = models.CharField(max_length=100)
    cooling_support = models.CharField(max_length=10)
    wattage = models.IntegerField()

class GraphicsCard(Product):
    brand = models.CharField(max_length=250, default="")
    gpu_chipset = models.CharField(max_length=250)
    memory_size = models.CharField(max_length=250)  
    memory_type = models.CharField(max_length=250) 
    clock_speed = models.CharField(max_length=250)
    wattage = models.IntegerField()

class HardDisk(Product):
    brand = models.CharField(max_length=250, default="")
    capacity = models.CharField(max_length=250) 
    form_factor = models.CharField(max_length=250) 
    rpm = models.IntegerField() 
    cache_size = models.CharField(max_length=250)
    wattage = models.IntegerField()

class Keyboards(Product):
    connection_type = models.CharField(max_length=250)  
    key_switch_type = models.CharField(max_length=250)  
    rgb = models.CharField(max_length=10)
    layout = models.CharField(max_length=250) 
    wattage = models.IntegerField()

class Monitor(Product):
    brand = models.CharField(max_length=250, default="")
    screen_size = models.DecimalField(max_digits=4, decimal_places=1)  
    resolution = models.CharField(max_length=250) 
    refresh_rate = models.CharField(max_length=250) 
    panel_type = models.CharField(max_length=250) 
    response_time = models.CharField(max_length=250)
    wattage = models.IntegerField()

class Motherboard(Product):
    brand = models.CharField(max_length=250, default="")
    chipset = models.CharField(max_length=250)
    socket_type = models.CharField(max_length=250)
    form_factor = models.CharField(max_length=250)
    max_memory = models.CharField(max_length=250) 
    memory_type = models.CharField(max_length=250) 
    wattage = models.IntegerField()

class Mouse(Product):
    connection_type = models.CharField(max_length=250)
    dpi = models.CharField(max_length=250)
    rgb = models.CharField(max_length=10)
    number_of_buttons = models.IntegerField()
    wattage = models.IntegerField()

class PowerSupply(Product):
    brand = models.CharField(max_length=250, default="")
    max_wattage = models.CharField(max_length=250)  
    efficiency_rating = models.CharField(max_length=250) 
    modular = models.CharField(max_length=10)
    wattage = models.IntegerField()

class Processors(Product):
    brand = models.CharField(max_length=250, default="")
    core = models.IntegerField() 
    thread = models.IntegerField() 
    clock_speed = models.DecimalField(decimal_places=2, max_digits=3)
    boost_clock = models.DecimalField(decimal_places=2, max_digits=3)
    socket_type = models.CharField(max_length=250)
    wattage = models.IntegerField()

class RAM(Product):
    capacity = models.CharField(max_length=250)
    memory_type = models.CharField(max_length=250)
    speed = models.IntegerField()
    wattage = models.IntegerField()

class SSD(Product):
    capacity = models.CharField(max_length=250)
    form_factor = models.CharField(max_length=250) 
    read_speed = models.CharField(max_length=250)
    write_speed = models.CharField(max_length=250)
    wattage = models.IntegerField()