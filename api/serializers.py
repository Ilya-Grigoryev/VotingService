from typing import Dict, Any

from api.models import Voting, Options, VotedUsers


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
        'name': voteduser.user.username,
        'id': voteduser.user.id
    }