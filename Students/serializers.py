from rest_framework.serializers import ModelSerializer
from .models import *

class Student_Serializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class Task_Serializer(ModelSerializer):

    class Meta:

        model = Task
        fields = "__all__"

class Student_Task_Serializer(ModelSerializer):

    all_tasks = Task_Serializer(many=True)

    class Meta:

        model=Student
        fields="__all__"

class Task_Data_Serializer(ModelSerializer):

    student_ref = Student_Serializer()

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