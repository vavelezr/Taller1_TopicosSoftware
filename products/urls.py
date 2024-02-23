from .views import *
from django.urls import path

urlpatterns = [
	path('', homePageView.as_view(), name='home'),
	path('create/', createProductView.as_view(), name='createProduct'),
	path('products/', showProductView.as_view(), name='showProduct'),
    path('products/create/success/', successProductView.as_view(), name='product_create_success'),
    path('products/<str:id>', showOneProductView.as_view(), name='show'),
    path('products/delete/<int:product_id>/', deleteProductView.as_view(), name='delete_product'),
]
