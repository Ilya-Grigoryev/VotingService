from django.urls import path

from api.views import voting_req, options_req, votedusers_req


urlpatterns = [
    path('voting/', voting_req),
    path('options/', options_req),
    path('votedusers/', votedusers_req)
]
