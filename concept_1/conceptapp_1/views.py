from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.

# #Converting a Single Model object 
# def student_detail(request):
#     stu=Student.objects.get(id=2)
#     print(1)
#     print(stu)
#     serialize=StudentSerializer(stu)
#     print(2)
#     print(serialize)
#     print(3)
#     print(serialize.data)
#     #Now model object is converted to Python native form
#     json_data=JSONRenderer().render(serialize.data)
#     print(4)
#     print(json_data)
#     #Now converted to JSON data
#     return HttpResponse(json_data, content_type='application/json')
#     #now sent to client

#Converting a Queryset: All student data
def student_detail(request):
    stu=Student.objects.all()
    print(1)
    print(stu)
    serialize=StudentSerializer(stu, many=True)
    print(2)
    print(serialize)
    print(3)
    print(serialize.data)
    #Now model object is converted to Python native form
    #json_data=JSONRenderer().render(serialize.data) No need in Method2
    #print(4)
    #print(json_data) No use in M2
    #Now converted to JSON data
    #return HttpResponse(json_data, content_type='application/json')
    #method2
    return JsonResponse(serialize.data, safe=False)
    #now sent to client