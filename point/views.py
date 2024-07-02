from django.shortcuts import render
from point.models import PontoColeta
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from point.serializers import PontoColetaSerializer


# Create your views here.
class PointCreateListView(generics.ListCreateAPIView):
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    queryset = PontoColeta.objects.all()
    serializer_class = PontoColetaSerializer
    
    
    
class PointRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    queryset = PontoColeta.objects.all()
    serializer_class = PontoColetaSerializer