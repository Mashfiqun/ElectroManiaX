from django import forms

class LaptopFilterForm(forms.Form):

    BRAND_CHOICES = [
        ('Intel', 'Intel'),
        ('AMD', 'AMD'),
        ('Apple', 'Apple')
    ]

    DISPLAY_SIZE_CHOICES = [
        ('13.3', '13 inch to 13.9 inch'),
        ('14', '14 inch to 14.9 inch'),
        ('15.6', '15 inch to 15.9 inch'),
        ('16', '16 inch')
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
