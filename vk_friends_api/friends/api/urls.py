from django.urls import path
from . import views

urlpatterns = [
    path('register/<slug:username>', views.register_new_user),
    path('friend_request/<int:user1_id>/<int:user2_id>', views.new_friend_request),
    path('requests_incoming_lsit/<int:user_id>', views.incoming_friend_requests),
    path('requests_outgoing_lsit/<int:user_id>', views.outgoing_friend_requests),
    path('friends_list/<int:user_id>', views.friends_list),
    path('status/<int:user1_id>/<int:user2_id>', views.friend_status),
    path('delete/<int:user1_id>/<int:user2_id>', views.delete_friend)
]
