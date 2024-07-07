from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def student_api_functions(request):
    if request.method=='GET':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        #api se get me id hi bhej rhe the
        idx=python_data.get('id', None)
        if idx is not None:
            stu=Student.objects.get(id=idx)
            serializer=StudentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        stu=Student.objects.all()
        serializer=StudentSerializer(stu, many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    
    if request.method=='POST':
        json_data_received=request.body
        stream=io.BytesIO(json_data_received)
        python_converted=JSONParser().parse(stream)
        
        serializer=StudentSerializer(data=python_converted)
        #serializer converts in into complex data(model object/queryset)
        if serializer.is_valid():
            serializer.save();#the object is saved to db
            #now respond back to client
            res={'msg':'Saved to database'}
            #res is python, convert to json and return 
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data=serializer.errors()
        return HttpResponse(json_data, content_type='application/json')
    
    if request.method=='PUT':
        json_data_received=request.body
        stream=io.BytesIO(json_data_received)
        python_converted=JSONParser().parse(stream)
        idx=python_converted.get('id')
        #name=python_converted.get('name')
        stu=Student.objects.get(id=idx)

        #update datathru serializer
        serializer=StudentSerializer(stu,data=python_converted, partial=True )
        if serializer.is_valid():
            serializer.save();#the object is updated in db
            #now respond back to client
            res={'msg':'Details updated in database'}
            #res is python, convert to json and return 
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data=serializer.errors()
        return HttpResponse(json_data, content_type='application/json')
    
    if request.method=='DELETE':
        json_data_received=request.body
        stream=io.BytesIO(json_data_received)
        python_converted=JSONParser().parse(stream)
        idx=python_converted.get('id')
        stu=Student.objects.get(id=idx)
        stu.delete()
        res={'msg':'Details updated after deletion'}
        #res is python, convert to json and return 

        return JsonResponse(res, safe=False)
        # json_data=JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type='application/json')






        












