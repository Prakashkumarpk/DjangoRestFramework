from rest_framework.serializers import ModelSerializer
from .models import *


class Book_Serializer(ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"

class Laptop_Serializer(ModelSerializer):

    class Meta:
        model = Laptop
        fields="__all__"