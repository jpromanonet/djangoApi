from django.http import JsonResponse
from django.shortcuts import render

# Third party imports
from rest_framework.response import Response
from rest_framework.views import APIView

def test_view(request):
    data = {
        'name': 'John',
        'age': 28
    }
    return JsonResponse(data, safe=False)