from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils import timezone
from rest_framework.decorators import api_view

from api.models import Voting, Options, VotedUsers
from api.serializers import VotedUsersSerializer
from api.serializers import serialize_vote, serialize_option, serialize_voteduser

from rest_framework.authtoken.models import Token


@api_view(['POST'])
def register_req(request):
    if request.method == 'POST':
        """
        {
            "first_name": "Илья",
            "last_name": "Григорьев",
            "username": "ilya",
            "email": "mail@mail.ru",
            "password": "1234"
        }
        """
        try:
            body = request.data
            user = User(first_name=body['first_name'],
                        last_name=body['last_name'],
                        username=body['username'],
                        email=body['email'],
                        password=make_password(body['password']))
            user.save()
        except:
            return JsonResponse({"status": 400, "description": "Bad Request"}, safe=False)
        return JsonResponse({"status": 200, "description": "OK"}, safe=False)


@api_view(['GET', 'POST'])
def voting_req(request):
    if request.method == 'GET':
        snippets = Voting.objects.all()
        serializers = [serialize_vote(snippet) for snippet in snippets]
        for serializer in serializers:
            vote_options = Options.objects.filter(voting_id=serializer['id'])
            serializer['options'] = [serialize_option(vote_option) for vote_option in vote_options]
            for option in serializer['options']:
                option_votedusers = VotedUsers.objects.filter(option_id=option['id'])
                option['users'] = [serialize_voteduser(voteduser) for voteduser in option_votedusers]
        return JsonResponse(serializers, safe=False)

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
            body = request.data
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


@api_view(['GET'])
def vote_req(request, vote_id):
    if request.method == 'GET':
        vote_snippet = Voting.objects.filter(id=vote_id)[0]
        serializer = serialize_vote(vote_snippet)
        vote_options = Options.objects.filter(voting_id=vote_id)
        serializer['options'] = [serialize_option(vote_option) for vote_option in vote_options]
        for option in serializer['options']:
            option_votedusers = VotedUsers.objects.filter(option_id=option['id'])
            option['users'] = [serialize_voteduser(voteduser) for voteduser in option_votedusers]
        return JsonResponse(serializer, safe=False)


@api_view(['GET', 'POST'])
def options_req(request):
    try:
        if not request.user:
            token = request.headers['Authorization'].replace('Token ', '')
            user = Token.objects.get(key=token).user
        else:
            user = request.user
    except:
        return JsonResponse({"status": 401, "description": " Unauthorized"}, safe=False)
    if request.method == 'GET':
        snippets = Options.objects.all()
        serializer = [serialize_option(snippet) for snippet in snippets]
        for option in serializer:
            option_votedusers = VotedUsers.objects.filter(option_id=option['id'])
            option['users'] = [serialize_voteduser(voteduser) for voteduser in option_votedusers]

        return JsonResponse(serializer, safe=False)

    elif request.method == 'POST':
        """
            Request body format:
            {
                "text": "Вариант ответа", 
                "voting_id": "1"
            }
        """
        try:
            body = request.data
            option = Options(text=body['text'],
                             voting_id=body['voting_id'])
            option.save()
            return JsonResponse({"status": 200, "description": "OK"}, safe=False)

        except:
            return JsonResponse({"status": 400, "description": "Bad Request"}, safe=False)


@api_view(['GET'])
def option_req(request, option_id):
    if request.method == 'GET':
        snippet = Options.objects.filter(id=option_id)[0]
        option = serialize_option(snippet)
        option_votedusers = VotedUsers.objects.filter(option_id=option['id'])
        option['users'] = [serialize_voteduser(voteduser) for voteduser in option_votedusers]

        return JsonResponse(option, safe=False)


@api_view(['GET', 'POST', 'DELETE'])
def votedusers_req(request):
    if request.method == 'GET':
        snippets = VotedUsers.objects.all()
        serializer = [serialize_voteduser(snippet) for snippet in snippets]
        return JsonResponse(serializer, safe=False)

    elif request.method == 'POST':
        """
            Request body format:
            {
                "option_id": "1"
            }
        """
        try:
            body = request.data
            if not request.user.is_authenticated:
                token = request.headers['Authorization'].replace('Token ', '')
                user = Token.objects.get(key=token).user
            else:
                user = request.user

            voted_user = VotedUsers(user=user,
                                    option_id=int(body['option_id']))
            voted_user.save()
            return JsonResponse({"status": 200, "description": "OK"}, safe=False)
        except Token.DoesNotExist:
            return JsonResponse({"status": 401, "description": "Invalid token."}, safe=False)

    elif request.method == 'DELETE':
        """
            Request body format:
            {
                "option_id": "1"
            }
        """
        try:
            body = request.data
            if not request.user.is_authenticated:
                token = request.headers['Authorization'].replace('Token ', '')
                user = Token.objects.get(key=token).user
            else:
                user = request.user
            voted_user = VotedUsers.objects.get(user=user,
                                                option_id=int(body['option_id']))
            voted_user.delete()
            return JsonResponse({"status": 200, "description": "OK"}, safe=False)
        except Token.DoesNotExist:
            return JsonResponse({"status": 401, "description": "Invalid token."}, safe=False)