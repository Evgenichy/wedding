from django.contrib import admin
from .models import Vote, Drinks, PresenceVote

admin.site.register(Vote)
admin.site.register(Drinks)
admin.site.register(PresenceVote)
