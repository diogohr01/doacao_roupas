from django.shortcuts import render
from donation.models import AgendamentoDoacao
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from donation.serializers import AgendamentoDoacaoSerializer


# Create your views here.
class DonationCreateListView(generics.ListCreateAPIView):
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    queryset = AgendamentoDoacao.objects.all()
    serializer_class = AgendamentoDoacaoSerializer
    
    
    
class DonationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
   # authentication_classes = (TokenAuthentication,)
   # permission_classes = (IsAuthenticated,)
    queryset = AgendamentoDoacao.objects.all()
    serializer_class = AgendamentoDoacaoSerializer
    
