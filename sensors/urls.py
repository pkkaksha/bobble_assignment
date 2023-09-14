from django.urls import path
from . import views

urlpatterns = [
    path('send_temp/', views.TemperatureView.as_view(),name="publish_temp"),
    path('fetch_temp/', views.TemperatureView.as_view(),name="fetch_temp")
]