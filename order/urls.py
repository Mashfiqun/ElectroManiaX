from django.urls import path


from .views import (
    Checkout,
    SaveOrder,
    OrderDetail
)


urlpatterns = [
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('save-order/', SaveOrder.as_view(), name='save-order'),
    path('order/<int:pk>/', OrderDetail.as_view(), name='order_detail'),
]