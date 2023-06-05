from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer
# from .serializers import TeacherSerializer
from .models import *
# def test(request):
#     data={
#         'name':'Kunal', 
#         'surname':"Pithadiya",
#         'age':21

#     }
#     return JsonResponse(data)

class super(APIView):
    def get(self,request,*args,**kwargs):
        # data_list = Student.objects.get(id=pk)
        data_list = Student.objects.all()
        # data = {
        #     'name':data_list.name,
        #     'roll':data_list.roll,
        #     'city':data_list.city,
        # }
        # data =  [{
        #     'name':i.name,
        #     'roll':i.roll,
        #     'city':i.city,
        # }for i in data_list]
        # data = [{
        #     'name':i.name,
        #     'roll':i.roll,
        #     'city':i.city
        #     }for i in data_list]
        # data = [i.name for i in data_list]
        data = []   #today
        for i in data_list:
            d = {
                'id':i.id,
                'name':i.name,
                'roll':i.roll,
                'city':i.city,
            }
            data.append(d)
        return Response(data)
    
# @APIView(['POST']) 


    def post(self,request,):
        data=request.data
        serializer=StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    def put(self,request,id,*args,**kwargs):
        item= Student.objects.get(id=id)
        serializer=StudentSerializer(item,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
        
        
       
    def patch(self,request,id,*args,**kwargs):
        item= Student.objects.get(id=id)
        serializer=StudentSerializer(item,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
      

    def delete(self,request,pk,*args,**kwargs):
        pass



class Students(APIView):
    def get(self,request,*args,**kwargs):
        Student_objs = Student.objects.all()
        serializer = StudentSerializer( Student_objs,many=True,)
        
        return Response(serializer.data)
    

    


        
    
