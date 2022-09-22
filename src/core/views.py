from django.http import JsonResponse
from django.shortcuts import render

# Third party imports
from rest_framework.response import Response
from rest_framework.views import APIView

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name': 'Dani ta chiquita',
            'Pregunta': '¿donde estamos?',
            'age': 25
        }
        return Response(data)