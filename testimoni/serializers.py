from rest_framework import serializers

from .models import Testimoni


class TestimoniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimoni
        fields = '__all__'