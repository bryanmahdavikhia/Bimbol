from rest_framework.serializers import ModelSerializer, SlugRelatedField
from .models import *


class ForumSerializer(ModelSerializer):
    class Meta:
        model = Forum
        fields = '__all__'

class ReplySerializer(ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'