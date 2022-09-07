from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import CategorySerializers
from .models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializers
