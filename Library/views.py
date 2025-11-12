from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import *
from .serializer import *

class BookView(ModelViewSet):

    queryset=Book.objects.all()
    serializer_class = Book_Serializer

class LaptopView(generics.ListCreateAPIView):

    # def get_queryset(self):
    #     return Laptop.objects.filter(brand="dell")
    
    def perform_create(self, serializer):
        serializer.save(user_type="High Performance")

    queryset=Laptop.objects.all()
    serializer_class = Laptop_Serializer

class LaptopViewById(generics.RetrieveUpdateDestroyAPIView):

    def perform_update(self, serializer):
        serializer.save(user_type="Low Performance")

    queryset=Laptop.objects.all()
    serializer_class = Laptop_Serializer