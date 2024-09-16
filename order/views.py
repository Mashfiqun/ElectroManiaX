from django.views import generic
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
import json
import uuid
from cart.carts import Cart
from product.models import Product
from .forms import CheckoutForm
from .models import Order, OrderItem
from cart.models import Coupon

class Checkout(LoginRequiredMixin, generic.View):
    login_url = reverse_lazy('login')
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {
            'form': form
        }
        return render(self.request, 'order/checkout.html', context)


    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST)

        if form.is_valid():
            data = form.cleaned_data
            print(data)
            return JsonResponse({
                'success': True,
                "data": data
            })
        else:
            return JsonResponse({
                'success': False,
                "errors": dict(form.errors)
            })

class SaveOrder(LoginRequiredMixin, generic.View):
    login_url = reverse_lazy('login')

    def post(self, *args, **kwargs):
        data = json.loads(self.request.body)
        cart = Cart(self.request)
        user_cart = Cart(self.request).cart
        if not user_cart:
            return JsonResponse({'success': False, 'error': 'Your cart is empty. Please add items to your cart before placing an order.'})
        product_ids = list(user_cart.keys())  
        products = Product.objects.filter(id__in=product_ids)
        
        ordered_products = []
        total_price = 0 


        for product in products:
            quantity = user_cart[str(product.id)]['quantity']
            price = product.price * quantity 
            total_price += price  

            order_item = OrderItem.objects.create(
                product=product,
                price=product.price,
                quantity=quantity
            )
            ordered_products.append(order_item)

        if data.get('coupon'): 
            coupon = Coupon.objects.get(code=data['coupon'])  
            total_price = coupon.apply_discount(total_price)  


        order = Order.objects.create(
            user=self.request.user,
            transaction_id=uuid.uuid4().hex,
            amount=total_price, 
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            city=data['city'],
            zip_code=data['zip_code'],
            address=data['address'],
            status='Received',
            coupon=coupon if data.get('coupon') else None
        )

        cart.clear()
        order.order_items.add(*ordered_products)

        order_confirmation_url = reverse_lazy('order_detail', kwargs={'pk': order.id})

        return JsonResponse({'success': True, 'order_url': order_confirmation_url})
class OrderDetail(LoginRequiredMixin, generic.DetailView):
    model = Order
    template_name = 'order/order_detail.html'  
    context_object_name = 'order'
