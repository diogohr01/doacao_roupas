from django.urls import path
from . import views


urlpatterns = [
    path('feedback/', views.FeedbackCreateListView.as_view(), name='feedback-create-list'),
    path('feedback/<int:pk>/', views.FeedbackRetrieveUpdateDestroyView.as_view(), name='feedback-detail-view'),
    path('feedback/rate/', views.FeedbackRateView.as_view(), name='feedback-rate-view'),

]