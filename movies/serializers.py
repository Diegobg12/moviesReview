from rest_framework import serializers
from .models import *

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'body', 'created_at',)
        model = Movie