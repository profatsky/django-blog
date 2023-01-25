from django.urls import path

from . import views

urlpatterns = [
    path('subscribe/', views.SubscribeToMailing.as_view(), name='subscribe')
]
