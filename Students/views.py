from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.

class StudentAPI(APIView):


    def get(self, request):
        all_students = Student.objects.all()

    #----------------------------Manual method without serializers-------------------------------
        # student_list = []

        # for s in all_students:
        #     student_dict = {
        #         "id":s.id,
        #         "name":s.name,
        #         "age": s.age
        #     }

        #     student_list.append(student_dict)
        # return Response(student_list)

    #----------------------------Using Serializers-----------------------------------------------
        student_data=Student_Serializer(all_students, many =True).data
        return Response(student_data)

    def post(self, request):
        print(request.data)

        new_student = Student(name = request.data['name'], age = request.data['age'])
        new_student.save()
        return Response("Student Created Successfully")
    
    def put(self, request, student_id):

        student_data = Student.objects.filter(id=student_id)
        student_data.update(name = request.data["name"], age = request.data["age"])
        return Response("Student Data Updated")

    def delete(self, request, student_id):

        student_data = Student.objects.get(id=student_id)
        student_data.delete()
        return Response("Student Data Deleted")
    
    # using serializes we are going to see the examples previously we used without serializers 

class TaskView(APIView):

# it is for all the data below i will write the code for the single data


    # def get(self, request):
    #     new_task= Task.objects.all()

    #     task_data = Task_Serializer(new_task, many=True).data
    #     return Response(task_data)  


# This is the code for both combined all data and single data using get

    def get(self, request, task_id=None):

        if task_id == None:
            new_task= Task.objects.all()
            task_data = Task_Data_Serializer(new_task, many=True).data
            return Response(task_data) 
        
        else:
            task = Task.objects.get(id = task_id)
            task_data = Task_Data_Serializer(task).data
            return Response(task_data)
    

    def post(self, request):
        new_task = Task_Serializer(data = request.data)

        if new_task.is_valid():
            new_task.save()

            return Response("New Task Added")
        else:

            return Response(new_task.errors)
    
    def patch(self, request, task_id):

        task = Task.objects.get(id=task_id)

        # why here partial = True meand if we did not give all the value it will just upload what are the values are given and throw 
        # error and it will update the field which has value 

        update_task = Task_Serializer(task, data= request.data, partial=True)

        if update_task.is_valid():
            update_task.save()
            return Response ("Task Updated")

        else:
            return (update_task.errors)
        
    def put(self, request, task_id):

        task = Task.objects.get(id=task_id)
        update_task = Task_Serializer(task, data= request.data, partial=True)

        if update_task.is_valid():

            update_task.save()
            return Response ("Task Updated")

        else:
            return (update_task.errors)
        
    # we cannot use Serializers for the delete method so we have to use the normal method

    def delete(self, request, task_id):

        task = Task.objects.get(id= task_id)
        task.delete()
        return Response("Data Deleted successfully")
        
    # It is the code for the single data using get method 

    # class TaskViewbyId(APIView):

    #     def get(self, request, task_id):

    #         task = Task.objects.get(id=task_id)
    #         task_data = Task_Serializer(task).data
    #         return Response(task_data)
    

class RankSheetView(APIView):

    def get(self, request, id=None):

        if id == None:

            new_rank = RankSheet.objects.all()
            rank_data = RankSheet_Serializer(new_rank, many=True).data
            return Response(rank_data)
        
        else:
            rank = RankSheet.objects.get(id=id)
            rank_data = RankSheet_Serializer(rank).data
            return Response(rank_data)


    def post(self, request):

        total_marks = request.data['tamil'] + request.data['english'] + request.data['maths'] + request.data['science'] + request.data['social_science']
        average_marks = total_marks/5

        if (request.data['tamil']>=35) and (request.data['english']>=35) and (request.data['maths']>=35) and (request.data['science']>=35) and (request.data['social_science']>=35):
            student_result =True
        else:
            student_result = False

        new_data = RankSheet(tamil=request.data['tamil'], english=request.data['english'], maths=request.data['maths'], 
                             science=request.data['science'], social_science=request.data['social_science'], total=total_marks,
                             average= average_marks, result=student_result)
        
        new_data.save()

        return Response("Data Saved")
    

    def put(self, request, id):


        update_marks = RankSheet.objects.filter(id=id)

        update_marks.update(tamil=request.data['tamil'], english=request.data['english'], maths=request.data['maths'], 
                             science=request.data['science'], social_science=request.data['social_science'], total=request.data['total'],
                             average= request.data['average'], result=request.data['result'])
        
    
        return Response("Data Updated Successfully")


