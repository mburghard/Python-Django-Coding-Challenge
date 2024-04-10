from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from rest_framework import generics, filters
from .models import Planet
from .serializers import PlanetSerializer

class PlanetListCreateView(generics.ListCreateAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name')
        terrains_query = self.request.query_params.get('terrains')
        climates_query = self.request.query_params.get('climates')
        min_population = self.request.query_params.get('min_population')
        max_population = self.request.query_params.get('max_population')

        if name is not None:
            queryset = queryset.filter(name__icontains=name)

        if terrains_query is not None:
            queryset = queryset.filter(terrains__icontains=terrains_query)

        if climates_query is not None:
            queryset = queryset.filter(climates__icontains=climates_query)

        population_filter = Q()
        if min_population is not None:
            population_filter &= Q(population__gte=min_population)
        if max_population is not None:
            population_filter &= Q(population__lte=max_population)

        queryset = queryset.filter(population_filter)
        return queryset

class PlanetRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

class PlanetListView(generics.ListAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
