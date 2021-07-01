from django.urls import path

from .views import ProductViewSet, UserCallView

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy'
    })),
    path('user', UserCallView.as_view())
]