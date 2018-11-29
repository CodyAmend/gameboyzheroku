from django.urls import path
from . import views
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('admin/order/<int:order_id>/', views.admin_order_detail, name='admin_order_detail'),
    path('admin/order/<int:order_id>/pdf/', views.admin_order_pdf, name='admin_order_pdf'),
    url(r'^orders_json/', views.OrderList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
