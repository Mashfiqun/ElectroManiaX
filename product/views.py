from typing import Any
from django.db.models import Q
from django.views import generic
from django.shortcuts import render
from django.core.paginator import (
    PageNotAnInteger,
    EmptyPage,
    InvalidPage,
    Paginator
)

from cart.carts import Cart
from .models import (
    Category,
    Product,
    Slider,
    Laptop,
    CPUCooler,
    Processors,
    Casing,
    GraphicsCard,
    HardDisk,
    Keyboards,
    Monitor,
    Motherboard,
    Mouse,
    PowerSupply,
    RAM,
    SSD,
)
from .forms import (
    LaptopFilterForm,
    CPUCoolerFilterForm,
    CasingFilterForm,
    GraphicsCardFilterForm,
    HardDiskFilterForm,
    KeyboardsFilterForm,
    MonitorFilterForm,
    MotherboardFilterForm,
    MouseFilterForm,
    PowerSupplyFilterForm,
    ProcessorFilterForm,
    RAMFilterForm,
    SSDFilterForm
)

class Home(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'featured_categories': Category.objects.filter(featured=True),
                'featured_products': Product.objects.filter(featured=True),
                'sliders': Slider.objects.filter(show=True)
            }
        )
        return context

class ProductDetails(generic.DetailView):
    model = Product
    template_name = 'product/product-details.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_products'] = self.get_object().related
        return context




class CategoryDetails(generic.ListView):
    model = Category
    template_name = 'product/category-details.html'
    slug_url_kwarg = 'slug'
    context_object_name = "products"
    def get_queryset(self):
        category_slug = self.kwargs.get('slug')
        category = Category.objects.get(slug=category_slug)
        
        if category.slug == 'laptop':
            queryset = Laptop.objects.filter(category=category)
        elif category.slug == 'cpu-cooler':
            queryset = CPUCooler.objects.filter(category=category)
        elif category.slug == 'casing':
            queryset = Casing.objects.filter(category=category)
        elif category.slug == 'graphics-cards':
            queryset = GraphicsCard.objects.filter(category=category)
        elif category.slug == 'hard-disk':
            queryset = HardDisk.objects.filter(category=category)
        elif category.slug == 'keyboard':
            queryset = Keyboards.objects.filter(category=category)
        elif category.slug == 'monitor':
            queryset = Monitor.objects.filter(category=category)
        elif category.slug == 'motherboard':
            queryset = Motherboard.objects.filter(category=category)
        elif category.slug == 'mouse':
            queryset = Mouse.objects.filter(category=category)
        elif category.slug == 'power-supply':
            queryset = PowerSupply.objects.filter(category=category)
        elif category.slug == 'processor':
            queryset = Processors.objects.filter(category=category)    
        elif category.slug == 'ram':
            queryset = RAM.objects.filter(category=category)
        else:
            queryset = Product.objects.filter(category=category)
        
        filter_params = self.request.GET
        if category.slug == 'laptop':
            if 'brand' in filter_params:
                queryset = queryset.filter(brand__in=filter_params.getlist('brand'))
            if 'display_size' in filter_params:
                display_sizes = filter_params.getlist('display_size')
                display_query = Q()

                for size in display_sizes:
                    if size == '13-13.9':
                        display_query |= Q(display_size__gte=13, display_size__lte=13.9)
                    elif size == '14-14.9':
                        display_query |= Q(display_size__gte=14, display_size__lte=14.9)
                    elif size == '15-15.9':
                        display_query |= Q(display_size__gte=15, display_size__lte=15.9)
                    elif size == '16+':
                        display_query |= Q(display_size__gte=16)

                if display_query:
                    queryset = queryset.filter(display_query)
            if 'ram_size' in filter_params:
                queryset = queryset.filter(ram_size__in=filter_params.getlist('ram_size'))
            if 'ram_type' in filter_params:
                queryset = queryset.filter(ram_type__in=filter_params.getlist('ram_type'))
            if 'storage_size' in filter_params:
                queryset = queryset.filter(storage_size__in=filter_params.getlist('storage_size'))
            if 'graphics_size' in filter_params:
                queryset = queryset.filter(graphics_size__in=filter_params.getlist('graphics_size'))
        elif category.slug == 'cpu-cooler':
            if 'brand' in filter_params:
                queryset = queryset.filter(brand__in=filter_params.getlist('brand'))
            if 'fan_speed' in filter_params:
                fan_speeds = filter_params.getlist('fan_speed')
                fan_speed_query = Q()

                for speed in fan_speeds:
                    if speed == '0-1000':
                        fan_speed_query |= Q(fan_speed__gte=0, fan_speed__lte=1000)
                    elif speed == '1001-2000':
                        fan_speed_query |= Q(fan_speed__gte=1001, fan_speed__lte=2000)
                    elif speed == '2000+':
                        fan_speed_query |= Q(fan_speed__gte=2001)

                if fan_speed_query:
                    queryset = queryset.filter(fan_speed_query)
            if 'cooler_type' in filter_params:
                queryset = queryset.filter(cooler_type__in=filter_params.getlist('cooler_type'))
            if 'rgb' in filter_params:
                queryset = queryset.filter(rgb__in=filter_params.getlist('rgb'))
        elif category.slug == 'casing':
            if 'brand' in filter_params:
                queryset = queryset.filter(brand__in=filter_params.getlist('brand'))
            if 'form_factor' in filter_params:
                queryset = queryset.filter(form_factor__in=filter_params.getlist('form_factor'))
            if 'material' in filter_params:
                queryset = queryset.filter(material__in=filter_params.getlist('material'))
            if 'color' in filter_params:
                queryset = queryset.filter(color__in=filter_params.getlist('color'))
            if 'cooling_support' in filter_params:
                queryset = queryset.filter(cooling_support__in=filter_params.getlist('cooling_support'))
        elif category.slug == 'graphics-cards':
            if 'brand' in filter_params:
                queryset = queryset.filter(brand__in=filter_params.getlist('brand'))
            if 'gpu_chipset' in filter_params:
                queryset = queryset.filter(gpu_chipset__in=filter_params.getlist('gpu_chipset'))
            if 'memory_size' in filter_params:
                queryset = queryset.filter(memory_size__in=filter_params.getlist('memory_size'))
            if 'memory_type' in filter_params:
                queryset = queryset.filter(memory_type__in=filter_params.getlist('memory_type'))
        elif category.slug == 'hard-disk':
            if 'brand' in filter_params:
                queryset = queryset.filter(brand__in=filter_params.getlist('brand'))
            if 'capacity' in filter_params:
                queryset = queryset.filter(capacity__in=filter_params.getlist('capacity'))
            if 'form_factor' in filter_params:
                queryset = queryset.filter(form_factor__in=filter_params.getlist('form_factor'))
            if 'rpm' in filter_params:
                queryset = queryset.filter(rpm__in=filter_params.getlist('rpm'))
        elif category.slug == 'keyboard':
            if 'connection_type' in filter_params:
                queryset = queryset.filter(connection_type__in=filter_params.getlist('connection_type'))
            if 'key_switch_type' in filter_params:
                queryset = queryset.filter(key_switch_type__in=filter_params.getlist('key_switch_type'))
            if 'rgb' in filter_params:
                queryset = queryset.filter(rgb__in=filter_params.getlist('rgb'))
        elif category.slug == 'monitor':
            if 'brand' in filter_params:
                queryset = queryset.filter(brand__in=filter_params.getlist('brand'))
            if 'screen_size' in filter_params:
                screen_sizes = filter_params.getlist('screen_size')
                screen_size_query = Q()

                for size in screen_sizes:
                    if size == '21-22':
                        screen_size_query |= Q(screen_size__gte=21, screen_size__lte=22)
                    elif size == '23-25':
                        screen_size_query |= Q(screen_size__gte=23, screen_size__lte=25)
                    elif size == '26-30':
                        screen_size_query |= Q(screen_size__gte=26, screen_size__lte=30)

                if screen_size_query:
                    queryset = queryset.filter(screen_size_query)
            if 'resolution' in filter_params:
                queryset = queryset.filter(resolution__in=filter_params.getlist('resolution'))
            if 'refresh_rate' in filter_params:
                queryset = queryset.filter(refresh_rate__in=filter_params.getlist('refresh_rate'))
            if 'panel_type' in filter_params:
                queryset = queryset.filter(panel_type__in=filter_params.getlist('panel_type'))
        elif category.slug == 'motherboard':
            if 'brand' in filter_params:
                queryset = queryset.filter(brand_type__in=filter_params.getlist('brand'))
            if 'socket_type' in filter_params:
                queryset = queryset.filter(socket_type__in=filter_params.getlist('socket_type'))
            if 'chipset' in filter_params:
                queryset = queryset.filter(chipset__in=filter_params.getlist('chipset'))
            if 'form_factor' in filter_params:
                queryset = queryset.filter(form_factor__in=filter_params.getlist('form_factor'))
            if 'max_memory' in filter_params:
                queryset = queryset.filter(max_memory__in=filter_params.getlist('max_memory'))
            if 'memory_type' in filter_params:
                queryset = queryset.filter(memory_type__in=filter_params.getlist('memory_type'))
        elif category.slug == 'mouse':
            if 'connection_type' in filter_params:
                queryset = queryset.filter(connection_type__in=filter_params.getlist('connection_type'))
            if 'dpi' in filter_params:
                queryset = queryset.filter(dpi__in=filter_params.getlist('dpi'))
            if 'rgb' in filter_params:
                queryset = queryset.filter(rgb__in=filter_params.getlist('rgb'))
        elif category.slug == 'power-supply':
            if 'brand' in filter_params:
                queryset = queryset.filter(brand__in=filter_params.getlist('brand'))
            if 'max_wattage' in filter_params:
                queryset = queryset.filter(max_wattage_type__in=filter_params.getlist('max_wattage'))
            if 'efficiency_rating' in filter_params:
                queryset = queryset.filter(efficiency_rating__in=filter_params.getlist('efficiency_rating'))
            if 'modular' in filter_params:
                queryset = queryset.filter(modular__in=filter_params.getlist('modular'))
        elif category.slug == 'processor':
            if 'brand' in filter_params:
                queryset = queryset.filter(brand__in=filter_params.getlist('brand'))
            if 'core' in filter_params:
                queryset = queryset.filter(core__in=filter_params.getlist('core'))
            if 'thread' in filter_params:
                queryset = queryset.filter(thread__in=filter_params.getlist('thread'))
            if 'clock_speed' in filter_params:
                clock_speeds = filter_params.getlist('clock_speed')
                clock_speed_query = Q()

                for speed in clock_speeds:
                    if speed == '2.4-3.4':
                        clock_speed_query |= Q(clock_speed__gte=2.4, clock_speed__lte=3.4)
                    elif speed == '3.5-3.9':
                        clock_speed_query |= Q(clock_speed__gte=3.5, clock_speed__lte=3.9)
                    elif speed == '4-5':
                        clock_speed_query |= Q(clock_speed__gte=4.0, clock_speed__lte=5.0)
                    elif speed == '5+':
                        clock_speed_query |= Q(clock_speed__gte=5.1)

                if clock_speed_query:
                    queryset = queryset.filter(clock_speed_query)
        elif category.slug == 'ram':
            if 'capacity' in filter_params:
                queryset = queryset.filter(capacity__in=filter_params.getlist('capacity'))
            if 'memory_type' in filter_params:
                queryset = queryset.filter(memory_type__in=filter_params.getlist('memory_type'))
            if 'speed' in filter_params:
                speeds = filter_params.getlist('speed')
                speed_query = Q()

                for speed in speeds:
                    if speed == '3000-4000':
                        speed_query |= Q(speed__gte=3000, speed__lte=4000)
                    elif speed == '4001-5000':
                        speed_query |= Q(speed__gte=4001, speed__lte=5000)
                    elif speed == '5001-6000':
                        speed_query |= Q(speed__gte=5001, speed__lte=6000)
                    elif speed == '6001-7000':
                        speed_query |= Q(speed__gte=6001, speed__lte=7000)

                if speed_query:
                    queryset = queryset.filter(speed_query)
        elif category.slug == 'ssd':
            if 'capacity' in filter_params:
                queryset = queryset.filter(capacity__in=filter_params.getlist('capacity'))
            if 'form_factor' in filter_params:
                queryset = queryset.filter(form_factor__in=filter_params.getlist('form_factor'))
            if 'read_speed' in filter_params:
                read_speeds = filter_params.getlist('read_speed')
                read_speed_query = Q()

                for speed in read_speeds:
                    if speed == '500-800':
                        read_speed_query |= Q(read_speed__gte=500, read_speed__lte=800)
                    elif speed == '801-1000':
                        read_speed_query |= Q(read_speed__gte=801, read_speed__lte=1000)
                    elif speed == '1001+':
                        read_speed_query |= Q(read_speed__gte=1001)

                if read_speed_query:
                    queryset = queryset.filter(read_speed_query)
            if 'write_speed' in filter_params:
                write_speeds = filter_params.getlist('write_speed')
                write_speed_query = Q()

                for speed in write_speeds:
                    if speed == '500-800':
                        write_speed_query |= Q(write_speed__gte=500, write_speed__lte=800)
                    elif speed == '801-1000':
                        write_speed_query |= Q(write_speed__gte=801, write_speed__lte=1000)
                    elif speed == '1001+':
                        write_speed_query |= Q(write_speed__gte=1001)

                if write_speed_query:
                    queryset = queryset.filter(write_speed_query)
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs.get('slug')
        category = Category.objects.get(slug=category_slug)

        if category_slug == 'laptop':
            context['filter_form'] = LaptopFilterForm(self.request.GET or None)
        elif category_slug == 'cpu-cooler':
            context['filter_form'] = CPUCoolerFilterForm(self.request.GET or None)
        elif category_slug == 'casing':
            context['filter_form'] = CasingFilterForm(self.request.GET or None)
        elif category_slug == 'graphics-cards':
            context['filter_form'] = GraphicsCardFilterForm(self.request.GET or None)
        elif category_slug == 'hard-disk':
            context['filter_form'] = HardDiskFilterForm(self.request.GET or None)
        elif category_slug == 'keyboard':
            context['filter_form'] = KeyboardsFilterForm(self.request.GET or None)
        elif category_slug == 'monitor':
            context['filter_form'] = MonitorFilterForm(self.request.GET or None)
        elif category_slug == 'motherboard':
            context['filter_form'] = MotherboardFilterForm(self.request.GET or None)
        elif category_slug == 'mouse':
            context['filter_form'] = MouseFilterForm(self.request.GET or None)
        elif category_slug == 'power-supply':
            context['filter_form'] = PowerSupplyFilterForm(self.request.GET or None)
        elif category_slug == 'processor':
            context['filter_form'] = ProcessorFilterForm(self.request.GET or None)
        elif category_slug == 'ram':
            context['filter_form'] = RAMFilterForm(self.request.GET or None)
        elif category_slug == 'ssd':
            context['filter_form'] = SSDFilterForm(self.request.GET or None)
        else:
            context['filter_form'] = None
        
        context['category'] = category
        return context
    

class CustomPaginator:
    def __init__(self, request, queryset, paginted_by) -> None:
        self.paginator = Paginator(queryset, paginted_by)
        self.paginated_by = paginted_by
        self.queryset = queryset
        self.page = request.GET.get('page', 1)

    def get_queryset(self):
            try:
                queryset = self.paginator.page(self.page)
            except PageNotAnInteger:
                queryset = self.paginator.page(1)
            except EmptyPage:
                queryset = self.paginator.page(1)
            except InvalidPage:
                queryset = self.paginator.page(1)    

            return queryset


class ProductList(generic.ListView):
    model = Product
    template_name = 'product/product-list.html'
    context_object_name = 'object_list'
    paginate_by = 8


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_obj = CustomPaginator(self.request, self.get_queryset(), self.paginate_by)
        quryset = page_obj.get_queryset()
        paginator = page_obj.paginator
        context['object_list'] = quryset
        context['paginator'] = paginator
        return context
        

class SearchProducts(generic.View):
    def get(self, *args, **kwargs):
        key = self.request.GET.get('key', '')
        products = Product.objects.filter(
            Q(title__icontains=key) |
            Q(category__title__icontains=key)
        )
        context = {
            'products': products,
            "key": key
        }
        return render(self.request, 'product/search-products.html', context)