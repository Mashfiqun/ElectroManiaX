from django.urls import path
from django.contrib.auth.views import (
    PasswordResetDoneView,
    PasswordResetCompleteView
)

from .views import (
    Login,
    Logout,
    Registration,
    ChangePassword,
    SendEmailToResetPassword,
    ResetPasswordConfirm,
    DashboardView,
    add_to_wishlist,
    wishlist_view,
    remove_from_wishlist
)


urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('registration/', Registration.as_view(), name='registration'),
    path('change-password/', ChangePassword.as_view(), name='change_password'),
    path('password-reset/', SendEmailToResetPassword.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', ResetPasswordConfirm.as_view(), name='password_reset_confirm'),
    path ('dashboard/',  DashboardView.as_view(), name='dashboard'),
    path('add-to-wishlist/<int:product_id>/', add_to_wishlist, name='add-to-wishlist'),
    path('wishlist/', wishlist_view, name='wishlist'),
    path('wishlist/remove/<int:product_id>/', remove_from_wishlist, name='remove_from_wishlist'),

]