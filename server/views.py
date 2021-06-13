from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Store, Comment
from .serializer import StoreSerializer, PopulatedStoreSerializer, CommentSerializer

class StoreListView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )


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

    permission_classes = (IsAuthenticatedOrReadOnly, )

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

    def delete(self, _request, pk):
        store_to_delete = self.get_store(pk=pk)
        store_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StoreFavouriteView(APIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request, pk):
        try:
            store_to_favourite = Store.objects.get(pk=pk)
            if request.user in store_to_favourite.favourited_by.all():
                store_to_favourite.favourited_by.remove(request.user.id)
            else:
                store_to_favourite.favourited_by.add(request.user.id)
            store_to_favourite.save()
            serialized_store = PopulatedStoreSerializer(store_to_favourite)
            return Response(serialized_store.data, status=status.HTTP_202_ACCEPTED)
        except Store.DoesNotExist:
            raise NotFound()

class CommentListView(APIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request, store_pk):
        request.data['store'] = store_pk
        request.data['owner'] = request.user.id
        serialized_comment = CommentSerializer(data=request.data)
        if serialized_comment.is_valid():
            serialized_comment.save()
            return Response(serialized_comment.data, status=status.HTTP_201_CREATED)
        return Response(serialized_comment.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class  CommentDetailView(APIView):

    def delete(self, request, _store_pk, comment_pk):
        try:
            comment_to_delete = Comment.objects.get(pk=comment_pk)
            if comment_to_delete.owner != request.user:
                raise PermissionDenied()
            comment_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            raise NotFound()
