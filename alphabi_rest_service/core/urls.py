from django.contrib import admin
from django.urls import path
from core.views import GeneralViewSet

urlpatterns = [
    path('api/<str:model>/', GeneralViewSet.as_view({'get': 'list'})),
]