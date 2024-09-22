from django.urls import path


from .views import (
    Checkout,
    SaveOrder,
    OrderDetail,
    all_orders
)


urlpatterns = [
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('save-order/', SaveOrder.as_view(), name='save-order'),
    path('order/<int:pk>/', OrderDetail.as_view(), name='order_detail'),
    path('orders/', all_orders, name='all-orders'),
]