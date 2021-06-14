from django.urls import path
from .views import (
    StoreListView,
    StoreDetailView,
    StoreFavouriteView,
    CommentListView,
    CommentDetailView
)

urlpatterns = [
    path('', StoreListView.as_view()),
    path('<int:pk>/', StoreDetailView.as_view()),
    path('<int:pk>/favourite/', StoreFavouriteView.as_view()),
    path('<int:store_pk>/comments/', CommentListView.as_view()),
    path('<int:_store_pk>/comments/<int:comment_pk>/', CommentDetailView.as_view())
]
