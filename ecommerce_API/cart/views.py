from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from .models import CartItem
from .serializers import *
from django.db.models import Q
from django.db.models.functions import Lower

class Cart(APIView):
    def get(self, request):
        obj = CartItem.objects.all()
        serializers = CartSerializer(obj, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)