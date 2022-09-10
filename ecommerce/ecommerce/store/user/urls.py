from rest_framework import routers
from django.urls import path, include
from . import views

from .views import ListUsers

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)


urlpatterns = [
    path('customers/', ListUsers.as_view()),
   
    
    path('login/', views.signin, name='signin'),
    path('logout/<int:id>/', views.signout, name='signout'),
    path('', include(router.urls))
]
