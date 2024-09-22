from django import forms
from .models import CPUCooler, Casing, GraphicsCard, HardDisk, Keyboards, Monitor, Motherboard, Mouse, PowerSupply, Processors, RAM, SSD

class LaptopFilterForm(forms.Form):

    BRAND_CHOICES = [
        ('Intel', 'Intel'),
        ('AMD', 'AMD'),
        ('Apple', 'Apple')
    ]

    DISPLAY_SIZE_CHOICES = [
        ('13-13.9', '13 inch to 13.9 inch'),
        ('14-14.9', '14 inch to 14.9 inch'),
        ('15-15.9', '15 inch to 15.9 inch'),
        ('16+', '16 inch')
    ]

    RAM_SIZE_CHOICES = [
        ('8GB', '8GB'),
        ('16GB', '16GB'),
        ('32GB', '32GB')
    ]

    RAM_TYPE_CHOICES = [
        ('DDR4', 'DDR4'),
        ('DDR5', 'DDR5')
    ]

    STORAGE_SIZE_CHOICES = [
        ('256GB', '256GB'),
        ('512GB', '512GB'),
        ('1TB', '1TB'),
        ('2TB', '2TB')
    ]

    GRAPHICS_SIZE_CHOICES = [
        ('Integrated', 'Integrated'),
        ('2GB', '2GB'),
        ('4GB', '4GB'),
        ('6GB', '6GB'),
        ('8GB', '8GB')
    ]

    brand = forms.MultipleChoiceField(
        choices=BRAND_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Brand"
    )

    display_size = forms.MultipleChoiceField(
        choices=DISPLAY_SIZE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Display Size"
    )

    ram_size = forms.MultipleChoiceField(
        choices=RAM_SIZE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="RAM Size"
    )

    ram_type = forms.MultipleChoiceField(
        choices=RAM_TYPE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="RAM Type"
    )

    storage_size = forms.MultipleChoiceField(
        choices=STORAGE_SIZE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Storage Size"
    )

    graphics_size = forms.MultipleChoiceField(
        choices=GRAPHICS_SIZE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Graphics Size"
    )

    min_price = forms.DecimalField(required=False, decimal_places=2, label="Min Price")
    max_price = forms.DecimalField(required=False, decimal_places=2, label="Max Price")

class CPUCoolerFilterForm(forms.Form):
    brand = forms.MultipleChoiceField(
        choices=[('Antec', 'Antec'), ('Cooler Master', 'Cooler Master'), ('DeepCool', 'DeepCool'), ('Xtreme', 'Xtreme')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Brand'
    )
    fan_speed = forms.MultipleChoiceField(
        choices=[('0-1000', 'Up to 1000 RPM'), ('1001-2000', '1001 RPM to 2000 RPM'), ('2000+', '2000 RPM & above')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Fan Speed'
    )
    cooler_type = forms.MultipleChoiceField(
        choices=[('Air', 'Air'), ('Liquid', 'Liquid')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Cooler Type'
    )
    rgb = forms.MultipleChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No')],
        widget=forms.CheckboxSelectMultiple, required=False, label='RGB'
    )
    min_price = forms.DecimalField(required=False, decimal_places=2, label="Min Price")
    max_price = forms.DecimalField(required=False, decimal_places=2, label="Max Price")

class CasingFilterForm(forms.Form):
    brand = forms.MultipleChoiceField(
        choices=[('Antec', 'Antec'), ('Cooler Master', 'Cooler Master'), ('DeepCool', 'DeepCool'), ('Xtreme', 'Xtreme')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Brand'
    )
    form_factor = forms.MultipleChoiceField(
        choices=[('ATX', 'ATX'), ('MicroATX', 'MicroATX'), ('ITX', 'ITX')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Form Factor'
    )
    material = forms.MultipleChoiceField(
        choices=[('Plastic', 'Plastic'), ('Mesh', 'Mesh'), ('Tampered Glass', 'Tampered Glass')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Material'
    )
    color = forms.MultipleChoiceField(
        choices=[('Black', 'Black'), ('White', 'White'), ('Gray', 'Gray')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Color'
    )
    cooling_support = forms.MultipleChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Cooling Support'
    )
    min_price = forms.DecimalField(required=False, decimal_places=2, label="Min Price")
    max_price = forms.DecimalField(required=False, decimal_places=2, label="Max Price")

class GraphicsCardFilterForm(forms.Form):
    brand = forms.MultipleChoiceField(
        choices=[('ASUS', 'ASUS'), ('Zotac', 'Zotac'), ('PNY', 'PNY'), ('Sapphire', 'Sapphire'), ('SPARKLE', 'SPARKLE')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Brand'
    )
    gpu_chipset = forms.MultipleChoiceField(
        choices=[('NVIDIA', 'NVIDIA'), ('AMD', 'AMD'), ('Intel', 'Intel')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Chipset'
    )
    memory_size = forms.MultipleChoiceField(
        choices=[('2GB', '2GB'), ('4GB', '4GB'), ('8GB', '8GB'), ('16GB', '16GB')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Memory'
    )
    memory_type = forms.MultipleChoiceField(
        choices=[('GDDR5', 'GDDR5'), ('GDDR6', 'GDDR6'), ('GDDR5X', 'GDDR5X'), ('GDDR6X', 'GDDR6X')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Memory Type'
    )
    min_price = forms.DecimalField(required=False, decimal_places=2, label="Min Price")
    max_price = forms.DecimalField(required=False, decimal_places=2, label="Max Price")

class HardDiskFilterForm(forms.Form):
    brand = forms.MultipleChoiceField(
        choices=[('Toshiba', 'Toshiba'), ('Seagate', 'Seagate'), ('Western Digital', 'Western Digital')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Brand'
    )
    capacity = forms.MultipleChoiceField(
        choices=[('1TB', '1TB'), ('2TB', '2TB'), ('4TB', '4TB'), ('8TB', '8TB')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Capacity'
    )
    form_factor = forms.MultipleChoiceField(
        choices=[('2.5', '2.5 inch'), ('3.5', '3.5 inch')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Form Factor'
    )
    rpm = forms.MultipleChoiceField(
        choices=[('5400', '5400 RPM'), ('5700', '5700 RPM'), ('5900', '5900 RPM'), ('7200', '7200 RPM')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Speed'
    )
    min_price = forms.DecimalField(required=False, decimal_places=2, label="Min Price")
    max_price = forms.DecimalField(required=False, decimal_places=2, label="Max Price")

class KeyboardsFilterForm(forms.Form):
    connection_type = forms.MultipleChoiceField(
        choices=[('Wired', 'Wired'), ('Wireless', 'Wireless'), ('Hybrid', 'Hybrid')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Connection Type'
    ) 
    key_switch_type = forms.MultipleChoiceField(
        choices=[('Membrane', 'Membrane'), ('Mechanical', 'Mechanical')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Switch Type'
    ) 
    rgb = forms.MultipleChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No')],
        widget=forms.CheckboxSelectMultiple, required=False, label='RGB'
    )
    min_price = forms.DecimalField(required=False, decimal_places=2, label="Min Price")
    max_price = forms.DecimalField(required=False, decimal_places=2, label="Max Price")

class MonitorFilterForm(forms.Form):
    brand = forms.MultipleChoiceField(
        choices=[('Samsung', 'Samsung'), ('GIGABYTE', 'GIGABYTE'), ('LG', 'LG')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Brand'
    )
    screen_size = forms.MultipleChoiceField(
        choices=[('21-22', '21" - 22"'), ('23-25', '23" - 25"'), ('26-30', '26" - 30"')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Screen Size'
    )
    resolution = forms.MultipleChoiceField(
        choices=[('1080p', '1080p'), ('1440p', '1440p'), ('4K', '4K')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Resolution'
    )
    refresh_rate = forms.MultipleChoiceField(
        choices=[('60Hz', '60Hz'), ('144Hz', '144Hz')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Refresh Rate'
    )
    panel_type = forms.MultipleChoiceField(
        choices=[('IPS', 'IPS'), ('TN', 'TN'), ('OLED', 'OLED')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Panel Type'
    )
    min_price = forms.DecimalField(required=False, decimal_places=2, label="Min Price")
    max_price = forms.DecimalField(required=False, decimal_places=2, label="Max Price")

class MotherboardFilterForm(forms.Form):
    brand = forms.MultipleChoiceField(
        choices=[('ASUS', 'ASUS'), ('GIGABYTE', 'GIGABYTE'), ('MSI', 'MSI')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Brand'
    )
    socket_type = forms.MultipleChoiceField(
        choices=[('AM4', 'AM4'), ('AM5', 'AM5'), ('TR4', 'TR4')],
        widget=forms.CheckboxSelectMultiple, required=False, label='CPU Sockets'
    )
    chipset = forms.MultipleChoiceField(
        choices=[('Intel', 'Intel'), ('AMD', 'AMD')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Chipset'
    )
    form_factor = forms.MultipleChoiceField(
        choices=[('ATX', 'ATX'), ('MicroATX', 'MicroATX')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Form Factor'
    )
    max_memory = forms.MultipleChoiceField(
        choices=[('32GB', '32GB'), ('64GB', '64GB')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Max Memory'
    )
    memory_type = forms.MultipleChoiceField(
        choices=[('DDR4', 'DDR4'), ('DDR5', 'DDR5')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Memory Type'
    )
    min_price = forms.DecimalField(required=False, decimal_places=2, label="Min Price")
    max_price = forms.DecimalField(required=False, decimal_places=2, label="Max Price")

class MouseFilterForm(forms.Form):
    connection_type = forms.MultipleChoiceField(
        choices=[('Wired', 'Wired'), ('Wireless', 'Wireless')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Connection Type'
    )
    dpi = forms.MultipleChoiceField(
        choices=[('400-3000', '400 - 3000 DPI'), ('3001-8000"', '3001 - 8000 DPI'), ('8001-20000"', '8001 - 20000 DPI')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Max DPI'
    )
    rgb = forms.MultipleChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No')],
        widget=forms.CheckboxSelectMultiple, required=False, label='RGB'
    )
    min_price = forms.DecimalField(required=False, decimal_places=2, label="Min Price")
    max_price = forms.DecimalField(required=False, decimal_places=2, label="Max Price")

class PowerSupplyFilterForm(forms.Form):
    brand = forms.MultipleChoiceField(
        choices=[('Antec', 'Antec'), ('Cooler Master', 'Cooler Master'), ('DeepCool', 'DeepCool'), ('Xtreme', 'Xtreme')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Brand'
    )
    max_wattage = forms.MultipleChoiceField(
        choices=[('500W', '500W'), ('650W', '650W'), ('750W', '750W')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Wattage'
    )
    efficiency_rating = forms.MultipleChoiceField(
        choices=[('80+ Bronze', '80+ Bronze'), ('80+ Gold', '80+ Gold')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Efficiency Rating'
    )
    modular = forms.MultipleChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No')],
        widget=forms.CheckboxSelectMultiple, required=False, label='RGB'
    )
    min_price = forms.DecimalField(required=False, decimal_places=2, label="Min Price")
    max_price = forms.DecimalField(required=False, decimal_places=2, label="Max Price")

class ProcessorFilterForm(forms.Form):
    brand = forms.MultipleChoiceField(
        choices=[('Intel', 'Intel'), ('AMD', 'AMD')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Brand'
    )
    core = forms.MultipleChoiceField(
        choices=[('4', '4'), ('6', '6'), ('8', '8'), ('12', '12'), ('16', '16')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Number of Cores'
    )
    thread = forms.MultipleChoiceField(
        choices=[('6', '6'), ('8', '8'), ('12', '12'), ('16', '16'), ('32', '32')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Number of Threads'
    )
    clock_speed = forms.MultipleChoiceField(
        choices=[('2.4-3.4', '2.40 GHz to 3.40 GHz'), ('3.5-3.9', '3.50 GHz to 3.90 GHz'), ('4-5', '4.00 GHz to 5.00 GHz'), ('5+', '5.10GHz and above')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Clock Speed'
    )
    min_price = forms.DecimalField(required=False, decimal_places=2, label="Min Price")
    max_price = forms.DecimalField(required=False, decimal_places=2, label="Max Price")

class RAMFilterForm(forms.Form):
    capacity = forms.MultipleChoiceField(
        choices=[('8GB', '8GB'), ('16GB', '16GB'), ('32GB', '32GB')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Capacity'
    )
    memory_type = forms.MultipleChoiceField(
        choices=[('DDR4', 'DDR4'), ('DDR5', 'DDR5')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Memory Type'
    )
    speed = forms.MultipleChoiceField(
        choices=[('3000-4000', '3000 - 4000MHz'), ('4001-5000', '4001 - 5000MHz'), ('5001-6000', '5001 - 6000MHz'), ('6001-7000', '6001 - 7000 RPM'), ('7001+', '7001 RPM or more')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Speed'
    )
    min_price = forms.DecimalField(required=False, decimal_places=2, label="Min Price")
    max_price = forms.DecimalField(required=False, decimal_places=2, label="Max Price")

class SSDFilterForm(forms.Form):
    capacity = forms.MultipleChoiceField(
        choices=[('256GB', '256GB'), ('512GB', '512GB'), ('1TB', '1TB')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Capacity'
    )
    form_factor = forms.MultipleChoiceField(
        choices=[('M.2', 'M.2'), ('2.5"', '2.5"')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Form Factor'
    )
    read_speed = forms.MultipleChoiceField(
        choices=[('500-800', '500 - 800 MB/s'), ('801-1000', '801 - 1000 MB/s'), ('1001+', '1001 MB/s and above')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Read Speed'
    )
    write_speed = forms.MultipleChoiceField(
        choices=[('500-800', '500 - 800 MB/s'), ('801-1000', '801 - 1000 MB/s'), ('1001+', '1001 MB/s and above')],
        widget=forms.CheckboxSelectMultiple, required=False, label='Write Speed'
    )
    min_price = forms.DecimalField(required=False, decimal_places=2, label="Min Price")
    max_price = forms.DecimalField(required=False, decimal_places=2, label="Max Price")

class PCBuilderForm(forms.Form):
    cpu_cooler = forms.ModelChoiceField(queryset=CPUCooler.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    casing = forms.ModelChoiceField(queryset=Casing.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    graphics_card = forms.ModelChoiceField(queryset=GraphicsCard.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    hard_disk = forms.ModelChoiceField(queryset=HardDisk.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    keyboard = forms.ModelChoiceField(queryset=Keyboards.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    monitor = forms.ModelChoiceField(queryset=Monitor.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    motherboard = forms.ModelChoiceField(queryset=Motherboard.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    mouse = forms.ModelChoiceField(queryset=Mouse.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    power_supply = forms.ModelChoiceField(queryset=PowerSupply.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    processor = forms.ModelChoiceField(queryset=Processors.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    ram = forms.ModelChoiceField(queryset=RAM.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    ssd = forms.ModelChoiceField(queryset=SSD.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-select'})
