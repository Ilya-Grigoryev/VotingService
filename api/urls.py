from django.urls import path
from api.views import voting_req, options_req, votedusers_req, vote_req, option_req, register_req, user_req, likes_req, \
    dislikes_req, comments_req, logout_req, change_password_req
from api.authentication import CustomAuthToken

urlpatterns = [
    path('voting/', voting_req),
    path('voting/<int:vote_id>/', vote_req),
    path('options/', options_req),
    path('options/<int:option_id>/', option_req),
    path('votedusers/', votedusers_req),
    path('login/', CustomAuthToken.as_view()),
    path('logout/', logout_req),
    path('register/', register_req),
    path('user/<int:user_id>/', user_req),
    path('likes/', likes_req),
    path('likes/<int:vote_id>/', likes_req),
    path('dislikes/', dislikes_req),
    path('comments/', comments_req),
    path('change_password/', change_password_req),
    # path('update_last_login/', update_last_login_req),

]
