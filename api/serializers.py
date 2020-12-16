from rest_framework.serializers import ModelSerializer

from api.models import Voting


class VotingSerializer(ModelSerializer):
    class Meta:
        model = Voting
        fields = ['title', 'description', 'user', 'start_date', 'end_date', 'status', 'type']
