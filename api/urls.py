from django.urls import path

from api.views import *
from api.authentication import CustomAuthToken

urlpatterns = [
    path('voting/', voting_req),
    path('voting/<int:vote_id>/', vote_req),
    path('options/', options_req),
    path('options/<int:option_id>/', option_req),
    path('votedusers/', votedusers_req),
    path('login/', CustomAuthToken.as_view()),
    path('logout/', logout_req),
    path('user_by_token/', user_by_token_req),
    path('register/', register_req),
    path('users/', user_req),
    path('user/<int:user_id>/', user_req),
    path('user/<int:user_id>/new_avatar/', change_avatar_req),
    path('likes/', likes_req),
    path('likes/<int:vote_id>/', likes_req),
    path('dislikes/', dislikes_req),
    path('comments/', comments_req),
    path('change_password/', change_password_req),
    path('delete_poll/', delete_poll_req),
    path('end_poll/', end_poll_req),
    path('start_poll/', start_poll_req),
    path('report/<int:id>/', abuse_report_req),
    path('report/', abuse_report_req),
    path('reports/<int:id>/', abuse_reports_req),
    path('reports/', abuse_reports_req),
    path('generate_code/<int:user_id>/', generate_code_req),
    path('change_poll/<int:poll_id>/', change_poll),
    path('check_username/<str:username>/', check_username),
]
