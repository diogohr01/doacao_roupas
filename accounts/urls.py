from django.urls import path
from . import views


urlpatterns = [
    path('accounts/', views.UserCreateListView.as_view(), name='accounts-create-list'),
    path('accounts/<int:pk>/', views.UserRetrieveUpdateDestroyView.as_view(), name='accounts-detail-view'),
    path('accounts/me/', views.LoginView.as_view(), name='accounts-detail-me'),
]
