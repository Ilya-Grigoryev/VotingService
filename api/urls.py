from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.views import VotingViewSet

router = SimpleRouter()
router.register('voting', VotingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
