from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from dotenv import load_dotenv
import os

load_dotenv()

# Create your views here.
def home(request):
    return JsonResponse({
        'id':1,
        'name':'Shyam lal',
        'post':'manager',
        'env':os.getenv('API_KEY')
    })


@csrf_exempt
def api(request):
    if request.method == 'POST':
        response = request.body
        data = json.loads(response)
        print(data[0]['id'])
        return JsonResponse(
            {
                'message':"success"
            }
        )
    return JsonResponse(
        {
            'message':"check your method"
        }
    )