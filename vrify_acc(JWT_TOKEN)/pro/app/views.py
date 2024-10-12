from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .email import send_verification_email
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework_simplejwt.tokens import UntypedToken, TokenError
from django.http import JsonResponse
import json




def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

# def dashboard(request):
#     return render(request,'dashboard.html')

# def loginauth(request):
#     if request.method == "POST":
#      data = request.body
#      data1 = json.loads(data)
#      email = data1.get('email')
#      password = data1.get('password')
#      print('email:', email)
#      print('password:', password)
#      user = authenticate(request, username=email, password=password)
#      print("user: ", user)

#      if user is not None:
#         return JsonResponse({"message": "Login successful", "redirect_url": "/dashboard/"}, status=200)
    
            
#      else:
#         return Response({"Error": "Email or password is incorrect"})    


class RegisterApi(APIView):
    def post(self,request):
        try:
            data = request.data
            print(data)
            serializer = UserSerializer(data = data)
            if serializer.is_valid():
                user = serializer.save()
                send_verification_email(user.email)
                return Response({
                    'status' : 200,
                    'message' : 'Registration Successfully',
                    'data' : serializer.data,
                }, status = status.HTTP_201_CREATED)
            
            return Response({
                'status' : 400,
                'message' : 'invalid data please try again',
                'error' : serializer.errors
            }, status = status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({
                'status' : 500,
                'message' : "internal server error",
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginApi(APIView):
    def post(self,request):
        try:
           data = request.body
           data1 = json.loads(data)
           email = data1.get('email')
           password = data1.get('password')
           print('email:', email)
           print('password:', password)
           user = authenticate(request, username=email, password=password)
           print("user: ", user)

           if user is not None:
            return JsonResponse({"message": "Login successful", "redirect_url": "/dashboard/"}, status=200)
    
            
           else:
              return Response({"Error": "Email or password is incorrect"})    

            
        except Exception as e:
            return Response({
                'status' : 500,
                'message' : "internal server error",
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        

    
        

        
 

        
    # def get(self,request):
    #     data = request.data    
    #     print(data)
    #     # email = data.get('email')
    #     # password = data.get('password')
    #     # print('email',email)
    #     # print('password',password)
    #     print(data['email'])
    #     print(data['password'])
    #     try:
            
    #         user = User.objects.get(email=data['email'], otp=data['password'])
    #         return render(self,'dashboard.html')
    #     except User.DoesNotExist:
    #         return Response({"Error" : "Email or password is incorrect"})   
        

     

class VerificationAccount(APIView):
        def get(self,request):
            token = request.query_params.get('token')
            try:
                UntypedToken(token)
                return Response({
                    'status' : 200,
                    'message' : 'Token is valid',
                },status=status.HTTP_200_OK)

            except TokenError:
                return Response({
                    'status' : 400,
                    'message' : 'Invalid Token',
                },status=status.HTTP_400_BAD_REQUEST)
                    
            except Exception as e:
                return Response({
                    'status' : 500,
                    'message' : 'INTERNAL SERVER ERROR',
                },status=status.HTTP_500_INTERNAL_SERVER_ERROR)        