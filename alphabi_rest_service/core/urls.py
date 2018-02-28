from django.contrib import admin
from django.urls import path
from core.views import (
    DataCreateAPIView,
    DataListAPIView,
    DataDetailAPIView,
    DataDeleteAPIView,
    DataUpdateAPIView
    )

urlpatterns = [
    path('data/create/', DataCreateAPIView.as_view()),
    path('data/', DataListAPIView.as_view()),
    path('data/<int:pk>/', DataDetailAPIView.as_view()),
    path('data/<int:pk>/delete/', DataDeleteAPIView.as_view()),
    path('data/<int:pk>/edit/', DataUpdateAPIView.as_view()),
]