from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

# Create your views here.

@api_view(['GET'])
def home(request):
    student_obj=Student.objects.all()   # yha student ka data student_obj me daaal diya
    serializer = StudentSerializer(student_obj, many=True)  #more than one data so used many=true
    return Response({"status": 200,"message": serializer.data})


@api_view(['POST'])
def post_student(request):
    serializer = StudentSerializer(data=request.data)
    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status':404,'error':serializer.errors ,'message':'something went wrong'})
    serializer.save()
    return Response({'status':200, 'payload':serializer.data,'message':'u send it'})



from rest_framework import generics

class StudentGeneric(generics.ListAPIView,generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer