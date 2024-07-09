from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class StudentAPIFunctions(View):
    def get(self, request, *args, **kwargs):
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
    
    def post(self, request, *args, **kwargs):
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
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    
    def put(self, request, *args, **kwargs):
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
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    
    def delete(self, request, *args, **kwargs):
        json_data_received=request.body
        stream=io.BytesIO(json_data_received)
        python_converted=JSONParser().parse(stream)
        idx=python_converted.get('id')
        if not idx:
                return JsonResponse({'msg': 'ID not provided'}, status=400)
            
        try:
            stu = Student.objects.get(id=idx)
            print(stu)
            stu.delete()
            res = {'msg': 'Details updated after deletion'}
        except ObjectDoesNotExist:
            return JsonResponse({'msg': 'Student not found'}, status=404)
            
        except Exception as e:
            return JsonResponse({'msg': str(e)}, status=400)

        return JsonResponse(res, safe=False)
        # json_data=JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type='application/json')









        












