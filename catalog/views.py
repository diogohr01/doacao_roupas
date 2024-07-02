from django.shortcuts import render
from catalog.models import CatalogoRoupas
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from catalog.serializers import CatalogoRoupasSerializer
# Create your views here.
class CatalogCreateListView(generics.ListCreateAPIView):
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    queryset = CatalogoRoupas.objects.all()
    serializer_class = CatalogoRoupasSerializer
    
    
    
class CatalogRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    queryset = CatalogoRoupas.objects.all()
    serializer_class = CatalogoRoupasSerializer
    