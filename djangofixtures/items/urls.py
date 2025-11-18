from django.urls import path
from .views import ItemListCreateView, ItemRetrieveUpdateDeleteView

urlpatterns = [
    path('items/', ItemListCreateView.as_view(), name='item-list'),
    path('items/<int:pk>/', ItemRetrieveUpdateDeleteView.as_view(), name='item-detail'),
]