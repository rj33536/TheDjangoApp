from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.index),
    path('catalog',views.catalog),
    path('products',views.products),
    path('checkout/<int:product_id>',views.checkout),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)