from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from . import models
from rest_framework import status


# Submits the data to the DB, displays all items & displays perevals by email
@api_view(['GET', 'POST'])
def submitData(request):
    # For displaying the items
    if request.method == 'GET':
        if request.GET.get('user__email'):
            perevals = models.Pereval_added.objects.filter(user__email=request.GET.get('user__email'))
        else: perevals = models.Pereval_added.objects.all()
        serializer = serializers.PerevalSerializer(perevals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = serializers.PerevalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


@api_view(['GET', 'PATCH'])
def pereval_detail_update(request, id):
    pereval = models.Pereval_added.objects.get(pk=id)
    if request.method == 'GET':
        serializer = serializers.PerevalSerializer(pereval)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PATCH':
        # So that you can't update a User model
        if request.data.get('user'):
            request.data.pop('user')
        serializer = serializers.PerevalSerializer(
            pereval, data=request.data, partial=True)

        if pereval.status == 'new':
            if serializer.is_valid():
                serializer.save()
                return Response({'state': '1'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        return Response({'state': '0',
                        'message': f"pereval status -> {pereval.status} (You can only edit objects with status -> 'new')"},
                        status=status.HTTP_400_BAD_REQUEST)

