from rest_framework.serializers import ModelSerializer
from .models import *


class Task_Serializer(ModelSerializer):

    class Meta:

        model = Task
        fields = "__all__"


# just for reference we can have multiple serializer for the single model 

# class Task_Serializer2(ModelSerializer):

#     class Meta:

#         model = Task
#         fields = ["task_name"]


class RankSheet_Serializer(ModelSerializer):

    class Meta:

        model=RankSheet
        fields = "__all__"