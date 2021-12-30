from rest_framework.serializers import ModelSerializer
from .models import Jadwal

class JadwalSerializer(ModelSerializer):
    class Meta:
        model = Jadwal
        fields = '__all__'