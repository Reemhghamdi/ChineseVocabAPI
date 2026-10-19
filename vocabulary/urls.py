from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import VocabularyViewSet

router = DefaultRouter()
router.register("words", VocabularyViewSet, basename="word")

urlpatterns = [
    path("", include(router.urls)),
]