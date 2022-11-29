from . import models
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from drf_extra_fields.fields import Base64ImageField


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


# Used "drf-extra-fields" module to easily convert Base64 to Image
class ImgSerializer(serializers.ModelSerializer):
    data = Base64ImageField()
    
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
    images = ImgSerializer(many=True)
    coords = CoordinatesSerializer()
    level = LevelSerializer()

    class Meta:
        model = models.Pereval_added
        fields = '__all__'
