from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.index,name='index'),
    path('catalog',views.catalog),
    path('products',views.products),
    path('checkout/<int:product_id>',views.checkout),
    
    path('accounts/login/',views.login,name="login"),
    path('accounts/logout/',views.logout,name="logout"),
    path('cart',views.mycart, name="cart"),
    path('register',views.register,name="register"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)