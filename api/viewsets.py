from rest_framework.viewsets import ModelViewSet

from api.models import Voting
from api.serializers import VotingSerializer


class VotingViewSet(ModelViewSet):
    queryset = Voting.objects.all()
    serializer_class = VotingSerializer
