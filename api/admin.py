from django.contrib import admin

from api.models import Voting, Options, VotedUsers, Likes, Dislikes, Comments, Profile

admin.site.register(Voting)
admin.site.register(Options)
admin.site.register(VotedUsers)
admin.site.register(Likes)
admin.site.register(Dislikes)
admin.site.register(Comments)
admin.site.register(Profile)
