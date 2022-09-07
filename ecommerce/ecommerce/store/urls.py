from django.urls import path, include
from rest_framework.authtoken import views as r_views
from rest_framework.authtoken.views import ObtainAuthToken

from . import views
from .views import index
urlpatterns = [
    path('', views.index, name='index'),

    path('category/', include('store.category.urls')),
    path('product/', include('store.product.urls')),
    path('user/', include('store.user.urls')),
    path('order/', include('store.order.urls')),
    path('store-token-auth/', r_views.obtain_auth_token, name='store_token_auth'),

]
