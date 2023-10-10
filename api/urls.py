from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from api.views import BookViewSet

router = SimpleRouter()
router.register('book', BookViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', include('rest_framework.urls')),
]