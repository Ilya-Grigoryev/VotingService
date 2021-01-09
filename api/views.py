from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils import timezone
from rest_framework.decorators import api_view

from api.models import Voting, Options, VotedUsers, Likes, Dislikes, Comments
from api.serializers import serialize_vote, serialize_option, serialize_voteduser, serialize_user, serialize_like, \
    serialize_dislike, serialize_comment

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
            "title": "Котики или собачки?",
            "description": "Кто милее?",
            "hours": 24,
            "options": ['Котики', 'Собачки']
        }
        """
        # try:
        body = request.data
        if not request.user.is_authenticated:
            token = request.headers['Authorization'].replace('Token ', '')
            user = Token.objects.get(key=token).user
        else:
            user = request.user
        end_date = timezone.now()
        end_date += timezone.timedelta(hours=int(body['hours']))
        vote = Voting(title=body['title'],
                      description=body['description'],
                      user=user,
                      start_date=timezone.now(),
                      end_date=end_date,
                      status="active",
                      type=0)
        vote.save()
        for option in body['options']:
            Options(text=option, voting=vote).save()

        return JsonResponse({"status": 200, "description": "OK"}, safe=False)

        # except:
        #     return JsonResponse({"status": 400, "description": "Bad Request"}, safe=False)


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
        if not request.user.is_authenticated:
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


@api_view(['GET', 'POST'])
def user_req(request, user_id):
    if request.method == 'GET':
        try:
            snippet = User.objects.get(id=user_id)
            user = serialize_user(snippet)
            return JsonResponse(user, safe=False)
        except:
            return JsonResponse({"status": 404, "description": "Bad Request"}, safe=False)

    elif request.method == 'POST':
        """
            Request body format:
            {
                "first_name": "Ilya",
                "last_name": "Grigoryev",
                "username": "grig",
                "email": "mail@mail.ru",
                "password": "1234"
            }
        """
        try:
            body = request.data
            if not request.user.is_authenticated:
                token = request.headers['Authorization'].replace('Token ', '')
                user = Token.objects.get(key=token).user
            else:
                user = request.user
            if not user.check_password(body['password']):
                return JsonResponse({"status": 401, "description": "Invalid password."}, safe=False)
            user.first_name = body['first_name']
            user.last_name = body['last_name']
            user.username = body['username']
            user.email = body['email']
            user.save()
            return JsonResponse({"status": 200, "description": "OK"}, safe=False)

        except Token.DoesNotExist:
            return JsonResponse({"status": 401, "description": "Invalid token."}, safe=False)


@api_view(['GET', 'POST'])
def likes_req(request):
    if request.method == 'GET':
        try:
            snippets = Likes.objects.all()
            likes = [serialize_like(snippet) for snippet in snippets]
            return JsonResponse(likes, safe=False)
        except:
            return JsonResponse({"status": 404, "description": "Bad Request"}, safe=False)


@api_view(['GET', 'POST'])
def dislikes_req(request):
    if request.method == 'GET':
        try:
            snippets = Dislikes.objects.all()
            dislikes = [serialize_dislike(snippet) for snippet in snippets]
            return JsonResponse(dislikes, safe=False)
        except:
            return JsonResponse({"status": 404, "description": "Bad Request"}, safe=False)


@api_view(['GET', 'POST'])
def comments_req(request):
    if request.method == 'GET':
        try:
            snippets = Comments.objects.all()
            comments = [serialize_comment(snippet) for snippet in snippets]
            return JsonResponse(comments, safe=False)
        except:
            return JsonResponse({"status": 404, "description": "Bad Request"}, safe=False)


@api_view(['POST'])
def comments_post(request):
    if request.method == 'POST':
        """
        {
            "user_id": "user_id",
            "id": "id",
            "voting_id": "voting_id",
            "text": "text",

        }
        """
        try:
            body = request.data
            comments = Comments(user_id=body['user_id'],
                        id=body['id'],
                        voting_id=body['voting_id'],
                        text=body['text'])

            comments.save()
        except:
            return JsonResponse({"status": 400, "description": "Bad Request"}, safe=False)
        return JsonResponse({"status": 200, "description": "OK"}, safe=False)


@api_view(['POST'])
def likes_post(request):
    if request.method == 'POST':
        """
        {
            "user_id": "user_id",
            "id": "id",
            "voting_id": "voting_id",
            

        }
        """
        try:
            body = request.data
            likes = Likes(user_id=body['user_id'],
                        id=body['id'],
                        voting_id=body['voting_id'])


            likes.save()
        except:
            return JsonResponse({"status": 400, "description": "Bad Request"}, safe=False)
        return JsonResponse({"status": 200, "description": "OK"}, safe=False)


@api_view(['POST'])
def dislikes_post(request):
    if request.method == 'POST':
        """
        Request body format:
        {
            "user_id": "user_id",
            "id": "id",
            "voting_id": "voting_id",


        }
        """
        try:
            body = request.data
            dislikes = Dislikes(user_id=body['user_id'],
                        id=body['id'],
                        voting_id=body['voting_id'])

            dislikes.save()
            return JsonResponse({"status": 200, "description": "OK"}, safe=False)
        except:
            return JsonResponse({"status": 400, "description": "Bad Request"}, safe=False)
        return JsonResponse({"status": 200, "description": "OK"}, safe=False)
