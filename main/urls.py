from django.urls import path

from .views import product_list, other_page, product_detail

app_name = 'main'
urlpatterns = [
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),
    path('<slug:category_slug>/', product_list, name='product_list_by_category'),
    path('others/<str:page>/', other_page, name='other'),
    path('', product_list, name='product_list'),
]