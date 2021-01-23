import datetime

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.utils import timezone

from api.models import Voting, Options, VotedUsers, Likes, Dislikes, Comments, Profile
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
            vote_id = serializer['id']
            vote_options = Options.objects.filter(voting_id=vote_id)
            serializer['options'] = [serialize_option(vote_option) for vote_option in vote_options]
            for option in serializer['options']:
                option_votedusers = VotedUsers.objects.filter(option_id=option['id'])
                option['users'] = [serialize_voteduser(voteduser) for voteduser in option_votedusers]
            vote_comments = Comments.objects.filter(voting_id=vote_id)
            serializer['comments'] = [serialize_comment(comment) for comment in vote_comments]
            vote_likes = Likes.objects.filter(voting_id=vote_id)
            serializer['likes'] = [serialize_like(like) for like in vote_likes]
            vote_dislikes = Dislikes.objects.filter(voting_id=vote_id)
            serializer['dislikes'] = [serialize_dislike(dislike) for dislike in vote_dislikes]
        return JsonResponse(serializers, safe=False)

    elif request.method == 'POST':
            """
            Request body format:
            {
                "title": "Котики или собачки?",
                "description": "Кто милее?",
                "hours": 24,
                "options": ['Котики', 'Собачки'],
                "image": file (or null),
                "start": "now" or "<datetime>"
            }
            """
        # try:
            body = dict(request.data)
            body['title'] = body['title'][0]
            body['description'] = body['description'][0]
            body['hours'] = body['hours'][0]
            if body['hours'] == 'infinite':
                body['hours'] = None
            else:
                body['hours'] = int(body['hours'])
            body['options'] = body['options'][0].split(',')
            body['file'] = body['file'][0]
            body['start'] = body['start'][0]
            if body['start'] == 'now':
                body['start'] = timezone.now() + timezone.timedelta(hours=3)
            else:
                body['start'] = datetime.datetime.strptime(body['start'], "%Y-%m-%d %H:%M")
            status = 'not started'
            if not request.user.is_authenticated:
                token = request.headers['Authorization'].replace('Token ', '')
                user = Token.objects.get(key=token).user
            else:
                user = request.user

            end_date = None
            if body['file'] == 'undefined':
                body['file'] = None
            if body['start'] == 'now':
                body['start'] = timezone.now() + timezone.timedelta(hours=3)

            if body['hours']:
                end_date = body['start'] + timezone.timedelta(hours=int(body['hours']))
            if end_date:
                vote = Voting(title=body['title'],
                              description=body['description'],
                              user=user,
                              image=body['file'],
                              start_date=body['start'],
                              end_date=end_date,
                              status=status,
                              type=0)
            else:
                vote = Voting(title=body['title'],
                              description=body['description'],
                              user=user,
                              image=body['file'],
                              start_date=body['start'],
                              status=status,
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
        vote_snippet = Voting.objects.get(id=vote_id)
        serializer = serialize_vote(vote_snippet)
        vote_options = Options.objects.filter(voting_id=vote_id)
        serializer['options'] = [serialize_option(vote_option) for vote_option in vote_options]
        for option in serializer['options']:
            option_votedusers = VotedUsers.objects.filter(option_id=option['id'])
            option['users'] = [serialize_voteduser(voteduser) for voteduser in option_votedusers]
        vote_comments = Comments.objects.filter(voting_id=vote_id)
        serializer['comments'] = [serialize_comment(comment) for comment in vote_comments]
        vote_likes = Likes.objects.filter(voting_id=vote_id)
        serializer['likes'] = [serialize_like(like) for like in vote_likes]
        vote_dislikes = Dislikes.objects.filter(voting_id=vote_id)
        serializer['dislikes'] = [serialize_dislike(dislike) for dislike in vote_dislikes]
        return JsonResponse(serializer, safe=False)


@api_view(['GET', 'POST'])
def options_req(request):
    if request.method == 'GET':
        snippets = Options.objects.all()
        serializer = [serialize_option(snippet) for snippet in snippets]
        for option in serializer:
            option_votedusers = VotedUsers.objects.filter(option_id=option['id'])
            option['users'] = [serialize_voteduser(voteduser) for voteduser in option_votedusers]

        return JsonResponse(serializer, safe=False)

    elif request.method == 'POST':
        try:
            if not request.user.is_authenticated:
                token = request.headers['Authorization'].replace('Token ', '')
                user = Token.objects.get(key=token).user
            else:
                user = request.user
        except:
            return JsonResponse({"status": 401, "description": " Unauthorized"}, safe=False)
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

            VotedUsers.objects.get_or_create(user=user,
                                             option_id=int(body['option_id']))
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


@api_view(['GET'])
def user_by_token_req(request):
    try:
        token = request.headers['Authorization'].replace('Token ', '')
        user = Token.objects.get(key=token).user
        profile = Profile.objects.get(user=user)
        return JsonResponse({'status': 200,
                             'avatar': profile.avatar.url if profile.avatar else 'null',
                             'token': token,
                             'id': user.id,
                             'email': user.email,
                             'username': user.username,
                             'first_name': user.first_name,
                             'last_name': user.last_name}, safe=False)
    except:
        return JsonResponse({"status": 401, "description": "Invalid token."}, safe=False)


@api_view(['GET', 'POST'])
def user_req(request, user_id=None):
    if request.method == 'GET':
        try:
            if user_id:
                snippet = User.objects.get(id=user_id)
                user = serialize_user(snippet)
                return JsonResponse(user, safe=False)
            else:
                snippets = User.objects.all()
                users = [serialize_user(snippet) for snippet in snippets]
                return JsonResponse(users, safe=False)
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


@api_view(['POST'])
def change_avatar_req(request, user_id):
    if request.method == 'POST':
        try:
            if not request.user.is_authenticated:
                token = request.headers['Authorization'].replace('Token ', '')
                user = Token.objects.get(key=token).user
            else:
                user = request.user
            file = dict(request.data)['file'][0]
            profile = Profile.objects.get(user=user)
            if profile.avatar:
                profile.avatar.delete()
            profile.avatar = file
            profile.save()
            return JsonResponse({"status": 200, "description": "OK", "avatar": profile.avatar.url}, safe=False)
        except:
            return JsonResponse({"status": 400, "description": "Bad Request"})


@api_view(['GET', 'POST'])
def likes_req(request, vote_id=None):
    if request.method == 'GET':
        try:
            if vote_id:
                snippets = Likes.objects.filter(voting_id=vote_id)
            else:
                snippets = Likes.objects.all()
            likes = [serialize_like(snippet) for snippet in snippets]
            return JsonResponse(likes, safe=False)
        except:
            return JsonResponse({"status": 404, "description": "Bad Request"}, safe=False)

    elif request.method == 'POST':
        """
        {
            "user_id": 1,
            "voting_id": 1
        }
        """
        try:
            if not request.user.is_authenticated:
                token = request.headers['Authorization'].replace('Token ', '')
                user = Token.objects.get(key=token).user
            else:
                user = request.user
            body = request.data
            if user.id != body['user_id']:
                return JsonResponse({"status": 401, "description": "Invalid token."}, safe=False)
            like, created = Likes.objects.get_or_create(user_id=body['user_id'],
                                                        voting_id=body['voting_id'])
            if not created:
                like.delete()
            else:
                try:
                    Dislikes.objects.get(user_id=body['user_id'], voting_id=body['voting_id']).delete()
                except:
                    pass
            return JsonResponse({"status": 200, "description": "OK"}, safe=False)
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

    elif request.method == 'POST':
        """
        {
            "user_id": 1,
            "voting_id": 1
        }
        """
        try:
            if not request.user.is_authenticated:
                token = request.headers['Authorization'].replace('Token ', '')
                user = Token.objects.get(key=token).user
            else:
                user = request.user
            body = request.data
            if user.id != body['user_id']:
                return JsonResponse({"status": 401, "description": "Invalid token."}, safe=False)
            dislike, created = Dislikes.objects.get_or_create(user_id=body['user_id'],
                                                              voting_id=body['voting_id'])
            if not created:
                dislike.delete()
            else:
                try:
                    Likes.objects.get(user_id=body['user_id'], voting_id=body['voting_id']).delete()
                except:
                    pass
            return JsonResponse({"status": 200, "description": "OK"}, safe=False)
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

    elif request.method == 'POST':
        """
        {
            "user_id": 1,
            "voting_id": 1,
            "text": "comment text"
        }
        """
        try:
            if not request.user.is_authenticated:
                token = request.headers['Authorization'].replace('Token ', '')
                user = Token.objects.get(key=token).user
            else:
                user = request.user
            body = request.data
            if user.id != body['user_id']:
                return JsonResponse({"status": 401, "description": "Invalid token."}, safe=False)
            comment = Comments(user_id=body['user_id'],
                               voting_id=body['voting_id'],
                               text=body['text'])
            comment.save()
            return JsonResponse({"status": 200, "description": "OK", "comment": serialize_comment(comment)}, safe=False)
        except:
            return JsonResponse({"status": 404, "description": "Bad Request"}, safe=False)


@api_view(['POST'])
def logout_req(request):
    if request.method == 'POST':
        try:
            token = request.headers['Authorization'].replace('Token ', '')
            Token.objects.get(key=token).delete()
            return JsonResponse({"status": 200, "description": "OK"}, safe=False)
        except:
            return JsonResponse({"status": 401, "description": "Invalid token."}, safe=False)


@api_view(['POST', 'DELETE'])
def change_password_req(request):
    if request.method == 'POST':
        try:
            body = request.data
            if not request.user.is_authenticated:
                token = request.headers['Authorization'].replace('Token ', '')
                user = Token.objects.get(key=token).user
            else:
                user = request.user
            if user.check_password(body['old_password']):
                return JsonResponse({"status": 401, "description": "Invalid password."}, safe=False)
            user.password = make_password(body['new_password'])
            user.save()
            return JsonResponse({"status": 200, "description": "OK"}, safe=False)
        except Token.DoesNotExist:
            return JsonResponse({"status": 401, "description": "Invalid token."}, safe=False)


@api_view(['POST'])
def delete_poll_req(request):
    if request.method == 'POST':
        try:
            body = request.data
            if not request.user.is_authenticated:
                token = request.headers['Authorization'].replace('Token ', '')
                user = Token.objects.get(key=token).user
            else:
                user = request.user
            Voting.objects.get(user=user, id=body['poll_id']).delete()
            return JsonResponse({"status": 200, "description": "OK"}, safe=False)
        except:
            return JsonResponse({"status": 401, "description": "Invalid token."}, safe=False)


@api_view(['POST'])
def end_poll_req(request):
    if request.method == 'POST':
        try:
            body = request.data
            if not request.user.is_authenticated:
                token = request.headers['Authorization'].replace('Token ', '')
                user = Token.objects.get(key=token).user
            else:
                user = request.user
            voting = Voting.objects.get(id=body['poll_id'])
            if voting.status == "active" or voting.status == "infinite":
                voting.end_date = timezone.now()
                voting.status = "ended"
                voting.save()
            return JsonResponse({"status": 200, "description": "OK"}, safe=False)
        except:
            return JsonResponse({"status": 401, "description": "Invalid token."}, safe=False)


@api_view(['POST'])
def start_poll_req(request):
    if request.method == 'POST':
        try:
            body = request.data
            if not request.user.is_authenticated:
                token = request.headers['Authorization'].replace('Token ', '')
                user = Token.objects.get(key=token).user
            else:
                user = request.user
            voting = Voting.objects.get(id=body['poll_id'])
            if voting.status == "not started":
                voting.start_date = timezone.now()
                if voting.end_date:
                    voting.status = "active"
                else:
                    voting.status = "infinite"
                voting.save()
            return JsonResponse({"status": 200, "description": "OK"}, safe=False)
        except:
            return JsonResponse({"status": 401, "description": "Invalid token."}, safe=False)
