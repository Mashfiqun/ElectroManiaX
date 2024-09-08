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
    Laptop
)
from .forms import LaptopFilterForm

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
        else:
            queryset = Product.objects.filter(category=category)
        
        filter_params = self.request.GET
        if category.slug == 'laptop':
            if 'brand' in filter_params:
                queryset = queryset.filter(brand__in=filter_params.getlist('brand'))
            if 'display_size' in filter_params:
                queryset = queryset.filter(display_size__in=filter_params.getlist('display_size'))
            if 'ram_size' in filter_params:
                queryset = queryset.filter(ram_size__in=filter_params.getlist('ram_size'))
            if 'ram_type' in filter_params:
                queryset = queryset.filter(ram_type__in=filter_params.getlist('ram_type'))
            if 'storage_size' in filter_params:
                queryset = queryset.filter(storage_size__in=filter_params.getlist('storage_size'))
            if 'graphics_size' in filter_params:
                queryset = queryset.filter(graphics_size__in=filter_params.getlist('graphics_size'))
        
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs.get('slug')
        category = Category.objects.get(slug=category_slug)

        if category_slug == 'laptop':
            context['filter_form'] = LaptopFilterForm(self.request.GET or None)
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

class LaptopListView(generic.ListView):
    model = Laptop
    template_name = 'product/category-details.html'
    context_object_name = 'product'

    slug_url_kwarg = 'slug'

    def get_queryset(self):
        queryset = Laptop.objects.all()
        form = LaptopFilterForm(self.request.GET)

        if form.is_valid():
            # Filter by brand
            brands = form.cleaned_data.get('brand')
            if brands:
                queryset = queryset.filter(brand__in=brands)

            # Filter by display size
            display_sizes = form.cleaned_data.get('display_size')
            if display_sizes:
                size_conditions = []
                for size in display_sizes:
                    if size == '13-13.9':
                        size_conditions.append(queryset.filter(display_size__gte=13, display_size__lte=13.9))
                    elif size == '14-14.9':
                        size_conditions.append(queryset.filter(display_size__gte=14, display_size__lte=14.9))
                    elif size == '15-15.9':
                        size_conditions.append(queryset.filter(display_size__gte=15, display_size__lte=15.9))
                    elif size == '16+':
                        size_conditions.append(queryset.filter(display_size__gte=16))

                if size_conditions:
                    queryset = queryset.filter(size_conditions.pop())

            # Filter by RAM size
            ram_sizes = form.cleaned_data.get('ram_size')
            if ram_sizes:
                queryset = queryset.filter(ram_size__in=ram_sizes)

            # Filter by RAM type
            ram_types = form.cleaned_data.get('ram_type')
            if ram_types:
                queryset = queryset.filter(ram_type__in=ram_types)

            # Filter by storage size
            storage_sizes = form.cleaned_data.get('storage_size')
            if storage_sizes:
                queryset = queryset.filter(storage_size__in=storage_sizes)

            # Filter by graphics size
            graphics_sizes = form.cleaned_data.get('graphics_size')
            if graphics_sizes:
                queryset = queryset.filter(graphics_size__in=graphics_sizes)

            # Filter by price range
            min_price = form.cleaned_data.get('min_price')
            if min_price:
                queryset = queryset.filter(price__gte=min_price)
            max_price = form.cleaned_data.get('max_price')
            if max_price:
                queryset = queryset.filter(price__lte=max_price)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = LaptopFilterForm(self.request.GET)
        return context
