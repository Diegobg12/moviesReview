from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', MovieDetail.as_view()),
    path('', MovieList.as_view()),
]
