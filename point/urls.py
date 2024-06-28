from django.urls import path
from . import views


urlpatterns = [
    path('point/', views.PointCreateListView.as_view(), name='point-create-list'),
    path('point/<int:pk>/', views.PointRetrieveUpdateDestroyView.as_view(), name='point-detail-view'),
    
]