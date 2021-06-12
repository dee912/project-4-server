from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import NotFound

from .models import Store
from .serializer import StoreSerializer, PopulatedStoreSerializer

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

class StoreDetailView(APIView):

    def get_store(self, pk):
        try:
            return Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            return NotFound()

    def get(self, _request, pk):
        store = self.get_store(pk=pk)
        serialized_store = PopulatedStoreSerializer(store)
        return Response(serialized_store.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        store_to_update = self.get_store(pk=pk)
        updated_store = StoreSerializer(store_to_update, data=request.data)
        if updated_store.is_valid():
            updated_store.save()
            return Response(updated_store.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_store.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
