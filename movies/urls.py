from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *


router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', MovieViewSet, basename='movies')
urlpatterns = router.urls
