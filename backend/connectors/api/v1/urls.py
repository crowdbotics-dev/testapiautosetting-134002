from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors134002ViewSet

router = DefaultRouter()
router.register(
    "testconnectors134002", Testconnectors134002ViewSet, basename="testconnectors134002"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
