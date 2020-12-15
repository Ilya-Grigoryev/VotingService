from django.shortcuts import render
from django.utils import timezone
from rest_framework.viewsets import ModelViewSet

from main.models import Voting, Options, VotedUsers

# Create your views here.


def main_page(request):
    context = {
        "date": timezone.now(),
        "voting": Voting.objects.all()
    }
    # print(context['voting'])
    return render(request, 'main.html', context)
