from django.shortcuts import render
from rest_framework import generics, permissions
from .permissions import *
from .models import *
from .serializers import *

# Create your views here.

class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer