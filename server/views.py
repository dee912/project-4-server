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
