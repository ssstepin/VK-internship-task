from django.contrib import admin
from .models import User, FriendRequest, FriendsPair

admin.site.register(User)
admin.site.register(FriendRequest)
admin.site.register(FriendsPair)
