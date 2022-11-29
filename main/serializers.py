from . import models
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class ImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Img
        fields = '__all__'


class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Coordinates
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Level_diff
        fields = '__all__'


# Used "drf_writable_nested" module to make writing data with nested serializers easier
class PerevalSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    user = UserSerializer()
    images = ImgSerializer()
    coords = CoordinatesSerializer()
    level = LevelSerializer()

    class Meta:
        model = models.Pereval_added
        fields = '__all__'