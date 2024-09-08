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
    banner = models.ImageField(upload_to='banners')
    show = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
