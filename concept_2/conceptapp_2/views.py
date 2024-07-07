from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

    
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body  # Store the JSON data from the request into a variable
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)

        serializer = StudentSerializer(data=pythondata)
        # Converts to complex data
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}

            # Send the message as response in JSON
            # As it is a Python dict
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')





    

