from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from django.contrib.auth import authenticate


class UserView(APIView):

    def post(self, request):
        new_user = User(username=request.data['username'], is_superuser=request.data['is_superuser'])
        new_user.set_password(request.data['password'])
        new_user.save()
        return Response ("User Created Successfully")
    
class UserLoginView(APIView):

    def post(self, request):

        user_verification = authenticate(username=request.data['username'], password= request.data['password'])

        if user_verification == None:
            return Response ("Username or Password is Invalid.. Try Again")
        else:
            return Response ("Valid User")