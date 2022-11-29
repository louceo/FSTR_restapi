from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from . import models
from rest_framework import status


@api_view(['GET', 'POST'])
def submitData(request):
    # for viewing 
    if request.method == 'GET':
        perevals = models.Pereval_added.objects.all()
        serializer = serializers.PerevalSerializer(perevals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = serializers.PerevalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

