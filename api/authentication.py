from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from api.models import Profile


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data,
                                               context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
        except:
            return Response({
                'status': 401,
                'description': 'Invalid username or password.'
            })
        profile = Profile.objects.get(user_id=user.pk)
        return Response({
            'avatar': profile.avatar.url if profile.avatar else 'null',
            'token': token.key,
            'id': user.pk,
            'is_admin': user.is_superuser,
            'email': user.email,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'status': 200
        })
