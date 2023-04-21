from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . models import User
from . serializer import UserSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def Homepage(request):
    return render(request, 'FIRSTAPPLICATION\homepage.html')


def Index(request):
    #all_objects = User.objects.all()
    return render(request, 'FIRSTAPPLICATION\index.html', )

#end point to fetch data
@csrf_exempt
def allusers(request):
    try:
        all_data = User.objects.all()
    except:
        return HttpResponse('Sorry.! No data found', status = 404)
    
    if request.method == 'GET':
        user = UserSerializer(all_data, many=True)
        return JsonResponse(user.data, safe = False)

    elif request.method == 'POST':
        input_data = JSONParser().parse(request)
        serializer = UserSerializer(data = input_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 200)
        else:
             return HttpResponse('Sorry.!!', status = 400)

@csrf_exempt
def single(request, pk):
    try:
        data = User.objects.get(pk = pk)
    except:
        return HttpResponse("Sorry.! not found", status = 404)
    if request.method == 'GET':
        user = UserSerializer(data)
        return JsonResponse(user.data, status = 200)   
    elif request.method == 'PUT':
        input_data = JSONParser().parse(request)
        serializer = UserSerializer(data = input_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 200)
        else:
             return HttpResponse('Sorry.!!', status = 400)
    elif request.method == 'DELETE':
        data.delete()
        return HttpResponse('Success', status = 200)
    


    

