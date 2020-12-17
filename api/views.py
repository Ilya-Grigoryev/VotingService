from django.http import JsonResponse
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.utils import json

from api.models import Voting, Options, VotedUsers
from api.serializers import VotingSerializer, OptionsSerializer, VotedUsersSerializer


@api_view(['GET', 'POST'])
def voting_req(request):
    if request.method == 'GET':
        snippets = Voting.objects.all()
        serializer = VotingSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        """
        Request body format:
        {
            "title": "Заголовок", 
            "description": "Описание", 
            "hours": 24, 
            "type": 0
        }
        """
        try:
            body = json.loads(request.body)
            end_date = timezone.now()
            end_date.hour += body.hours
            vote = Voting(title=body['title'],
                          description=body['description'],
                          user=request.user,
                          start_date=timezone.now(),
                          end_date=end_date,
                          status="active",
                          type=body['type'])
            vote.save()
            return JsonResponse({"status": 200, "description": "OK"}, safe=False)

        except:
            return JsonResponse({"status": 400, "description": "Bad Request"}, safe=False)


@api_view(['GET', 'POST'])
def options_req(request):
    if request.method == 'GET':
        snippets = Options.objects.all()
        serializer = OptionsSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        """
            Request body format:
            {
                "text": "Вариант ответа", 
                "voting_id": "1"
            }
        """
        try:
            body = json.loads(request.body)
            option = Options(text=body['text'],
                             voting_id=body['voting_id'])
            option.save()
            return JsonResponse({"status": 200, "description": "OK"}, safe=False)

        except:
            return JsonResponse({"status": 400, "description": "Bad Request"}, safe=False)


@api_view(['GET', 'POST'])
def votedusers_req(request):
    if request.method == 'GET':
        snippets = VotedUsers.objects.all()
        serializer = VotedUsersSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        """
            Request body format:
            {
                "option_id": "1"
            }
        """
        try:
            body = json.loads(request.body)
            voted_user = VotedUsers(user=request.user,
                                    option_id=body['option_id'])
            voted_user.save()
            return JsonResponse({"status": 200, "description": "OK"}, safe=False)

        except:
            return JsonResponse({"status": 400, "description": "Bad Request"}, safe=False)
