from typing import Dict, Any

from api.models import Voting, VotedUsers


def serialize_vote(vote) -> Dict[str, Any]:
    return {
        'title': vote.title,
        'description': vote.description,
        'user': {'name': vote.user.username, 'id': vote.user.id},
        'start_date': vote.start_date,
        'end_date': vote.end_date,
        'status': vote.status,
        'type': vote.type,
        'id': vote.id
    }


def serialize_option(option) -> Dict[str, Any]:
    return {
        'text': option.text,
        'id': option.id
    }


def serialize_voteduser(voteduser) -> Dict[str, Any]:
    return {
        'user': {
            'name': voteduser.user.username,
            'id': voteduser.user.id
        },
        'option id': voteduser.option_id,
        'voting_id': voteduser.option.voting_id
    }


def serialize_user(user) -> Dict[str, Any]:
    return {
        'email': user.email,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'polls_count': len(Voting.objects.filter(user_id=user.id)),
        'vote_count': len(VotedUsers.objects.filter(user_id=user.id))
    }