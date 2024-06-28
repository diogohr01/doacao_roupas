from django.urls import path
from . import views


urlpatterns = [
    path('catalog/', views.CatalogCreateListView.as_view(), name='catalog-create-list'),
    path('catalog/<int:pk>/', views.CatalogRetrieveUpdateDestroyView.as_view(), name='catalog-detail-view'),
    
]