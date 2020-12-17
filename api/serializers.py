from rest_framework.serializers import ModelSerializer

from api.models import Voting, Options, VotedUsers


class VotingSerializer(ModelSerializer):
    class Meta:
        model = Voting
        fields = ['title', 'description', 'user', 'start_date', 'end_date', 'status', 'type', 'id']


class OptionsSerializer(ModelSerializer):
    class Meta:
        model = Options
        fields = ['text', 'voting', 'id']


class VotedUsersSerializer(ModelSerializer):
    class Meta:
        model = VotedUsers
        fields = ['user', 'option', 'id']
