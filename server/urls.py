from django.urls import path
from .views import StoreListView, StoreDetailView

urlpatterns = [
    path('', StoreListView.as_view()),
    path('<int:pk>/', StoreDetailView.as_view())
]
