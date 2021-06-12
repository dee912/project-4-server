from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Store
from .serializer import StoreSerializer

class StoreListView(APIView):

    def get(self, _request):
        stores = Store.objects.all()
        serialized_stores = StoreSerializer(stores, many=True)
        return Response(serialized_stores.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        new_store = StoreSerializer(data=request.data)

        if new_store.is_valid():
            new_store.save()
            return Response(new_store.data, status=status.HTTP_201_CREATED)
        return Response(new_store.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
