from django.urls import path
from . import views


urlpatterns = [
    path('donation/', views.DonationCreateListView.as_view(), name='donation-create-list'),
    path('donation/<int:pk>/', views.DonationRetrieveUpdateDestroyView.as_view(), name='donation-detail-view'),
    
]