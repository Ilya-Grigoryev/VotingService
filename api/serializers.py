from typing import Dict, Any

from django.utils import timezone

from api.models import Voting, VotedUsers, Profile


def serialize_vote(vote) -> Dict[str, Any]:
    if vote.status == 'active':
        if vote.end_date and vote.end_date < timezone.now() + timezone.timedelta(hours=3):
            vote.status = 'ended'
    elif vote.status == 'not started' and vote.start_date < timezone.now() + timezone.timedelta(hours=3):
        vote.status = 'active'
        vote.save()
    return {
        'title': vote.title,
        'description': vote.description,
        'user': {'name': vote.user.username, 'id': vote.user.id},
        'image_url': vote.image.url if vote.image else 'null',
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
    profile = Profile.objects.get(user_id=voteduser.user_id)
    return {
        'user': {
            'name': voteduser.user.username,
            'id': voteduser.user.id,
            'avatar': profile.avatar.url if profile.avatar else 'null'
        },
        'option id': voteduser.option_id,
        'voting_id': voteduser.option.voting_id
    }


def serialize_user(user) -> Dict[str, Any]:
    profile = Profile.objects.get(user=user)
    return {
        'id': user.id,
        'avatar': profile.avatar.url if profile.avatar else 'null',
        'status': profile.status,
        'email': user.email,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'polls_count': len(Voting.objects.filter(user_id=user.id)),
        'vote_count': len(VotedUsers.objects.filter(user_id=user.id))
    }


def serialize_like(like) -> Dict[str, Any]:
    return {
        'id': like.id,
        'voting_id': like.voting_id,
        'user_id': like.user_id
    }


def serialize_dislike(dislike) -> Dict[str, Any]:
    return {
        'id': dislike.id,
        'voting_id': dislike.voting_id,
        'user_id': dislike.user_id
    }


def serialize_comment(comment) -> Dict[str, Any]:
    profile = Profile.objects.get(user_id=comment.user_id)
    return {
        'id': comment.id,
        'voting_id': comment.voting_id,
        'author': {
            'name': comment.user.username,
            'id': comment.user_id,
            'avatar': profile.avatar.url if profile.avatar else 'null'
        },
        'text': comment.text
    }


def serialize_message(message) -> Dict[str, Any]:
    profile = Profile.objects.get(user_id=message.user_id)
    return {
        'id': message.id,
        'user': {
            'name': message.user.username,
            'id': message.user_id,
            'avatar': profile.avatar.url if profile.avatar else 'null'
        },
        'text': message.text
    }


def serialize_report(report) -> Dict[str, Any]:
    profile = Profile.objects.get(user_id=report.user_id)
    return {
        'id': report.id,
        'user': {
            'name': report.user.username,
            'id': report.user_id,
            'avatar': profile.avatar.url if profile.avatar else 'null'
        },
        'title': report.title,
        'description': report.description,
        'status': report.status,
        'image': report.image.url if report.image else 'null'
    }
