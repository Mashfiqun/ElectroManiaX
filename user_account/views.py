import copy

from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from cart.carts import Cart
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetConfirmView
)
from django.contrib.auth.decorators import login_required
from cart.carts import Cart
from .forms import (
    LoginForm,
    UserRegistrationForm,
    ChangePasswordForm,
    SendEmailForm,
    ResetPasswordConfirmForm
)
from .mixins import (
    LogoutRequiredMixin
)
from order.models import Order
from product.models import Category
from .models import Wishlist, Product
@method_decorator(never_cache, name='dispatch')
class Login(LogoutRequiredMixin, generic.View):
    def get(self, *args, **kwargs):
        form = LoginForm()
        context = {
            "form": form
        }
        return render(self.request, 'account/login.html', context)

    def post(self, *args, **kwargs):
        form = LoginForm(self.request.POST)

        if form.is_valid():
            user = authenticate(
                self.request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(self.request, user)
                return redirect('home')

            else:
                messages.warning(self.request, "Wrong credentials")
                return redirect('login')

        return render(self.request, 'account/login.html', {"form": form})


class Logout(generic.View):
    def get(self, *args, **kwargs):
        cart = Cart(self.request)
        current_cart = copy.deepcopy(cart.cart)
        coupon = copy.deepcopy(cart.coupon)
        logout(self.request)
        cart.restore_after_logout(current_cart, coupon)
        return redirect('login')



@method_decorator(never_cache, name='dispatch')
class Registration(LogoutRequiredMixin, generic.CreateView):
    template_name = 'account/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, "Registration Successfull !")
        return super().form_valid(form)


@method_decorator(never_cache, name='dispatch')
class ChangePassword(LoginRequiredMixin, generic.FormView):
    template_name = 'account/change_password.html'
    form_class = ChangePasswordForm
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('login')

    def get_form_kwargs(self):
        context = super().get_form_kwargs()
        context['user'] = self.request.user
        return context

    def form_valid(self, form):
        user = self.request.user
        user.set_password(form.cleaned_data.get('new_password1'))
        user.save()
        messages.success(self.request, "Password changed Successfully !")
        return super().form_valid(form)


class SendEmailToResetPassword(PasswordResetView):
    template_name = 'account/password_reset.html'
    form_class = SendEmailForm


class ResetPasswordConfirm(PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    form_class = ResetPasswordConfirmForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, "Password reset successfully !")
        return super().form_valid(form)

@method_decorator(never_cache, name='dispatch')
class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'dashboard.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        join_date = user.date_joined.strftime('%B %d, %Y')

        recent_orders = Order.objects.filter(user=user).order_by('-created_date')[:5]

        categories = Category.objects.all()[:5] 

        context.update({
            'user_name': user.username,
            'user_email': user.email,
            'member_since': join_date,
            'recent_orders': recent_orders,
            'categories': categories,
        })

        return context



def add_to_wishlist(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        Wishlist.objects.get_or_create(user=request.user, product=product)
        return redirect('wishlist')
    return redirect('login')

def wishlist_view(request):
    if request.user.is_authenticated:
        wishlist_items = Wishlist.objects.filter(user=request.user)
        return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})
    return redirect('login') 
     
@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item = get_object_or_404(Wishlist, user=request.user, product=product)
    wishlist_item.delete()
    return redirect('wishlist')


def add_to_cart_wishlist(request, product_id):
    if request.user.is_authenticated:
        cart = Cart(request)
        cart.update(product_id)
        return redirect('cart')
    return redirect('login')