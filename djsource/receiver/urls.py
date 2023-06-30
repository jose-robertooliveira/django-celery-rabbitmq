from django.urls import path, include
from rest_framework import routers
from .views import PropostaViewSet


router = routers.DefaultRouter()
router.register(r'', PropostaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]