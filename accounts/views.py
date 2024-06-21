from rest_framework import generics
from accounts.models import User
from accounts.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated



class UserCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    

    
class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
   