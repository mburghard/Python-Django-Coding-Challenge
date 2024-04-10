from django.contrib import admin
from django.urls import path
from swdbApp.views import PlanetListCreateView, PlanetRetrieveUpdateDestroyView, PlanetListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('planets/', PlanetListCreateView.as_view()),
    path('planets/<int:pk>/', PlanetRetrieveUpdateDestroyView.as_view()),
]