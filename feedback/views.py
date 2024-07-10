
from feedback.models import Feedback
from rest_framework import generics
from feedback.serializers import FeedbackSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from feedback.models import Feedback
from django.db.models import Avg



class FeedbackCreateListView(generics.ListCreateAPIView):
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    
class FeedbackRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    
class FeedbackRateView(APIView):
    def get(self, request):
        rate = Feedback.objects.aggregate(Avg('stars'))['stars__avg']
        if rate:
            rate = round(rate, 1)
        return Response({'rate': rate})
    