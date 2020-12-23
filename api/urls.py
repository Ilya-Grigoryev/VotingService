from django.urls import path
from api.views import voting_req, options_req, votedusers_req, vote_req, option_req
from api.authentication import CustomAuthToken

urlpatterns = [
    path('voting/', voting_req),
    path('voting/<int:vote_id>/', vote_req),
    path('options/', options_req),
    path('options/<int:option_id>/', option_req),
    path('votedusers/', votedusers_req),
    path('login/', CustomAuthToken.as_view()),
]
