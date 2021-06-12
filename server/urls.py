from django.urls import path
from .views import StoreListView

urlpatterns = [
    path('', StoreListView.as_view())
]
