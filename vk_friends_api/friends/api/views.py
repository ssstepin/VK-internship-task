from .models import User, FriendRequest, FriendsPair
from .serializers import UserSerializer, FriendRequestSerializer, FriendsPairSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q



@api_view(['POST'])
def register_new_user(request, username):
    serializer = UserSerializer(data={"username": username})
    if serializer.is_valid():
        if User.objects.filter(username=username).exists():
            return Response(status=status.HTTP_409_CONFLICT)
        else:
            serializer.save()
            return Response({"new_user": serializer.data}, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def new_friend_request(request, user1_id, user2_id):
    serializer = FriendRequestSerializer(data=
    {
        "user1_id": user1_id,
        "user2_id": user2_id
    }
    )
    if serializer.is_valid():
        if FriendRequest.objects.filter(user1_id=user1_id, user2_id=user2_id).exists():
            return Response({"message": "This request already exists."}, status=status.HTTP_409_CONFLICT)
        elif user1_id == user2_id:
            return Response({"message": "Can't send     request to the same user."}, status=status.HTTP_403_FORBIDDEN)
        elif FriendsPair.objects.filter(user1_id=user1_id,
                                        user2_id=user2_id).exists() or FriendsPair.objects.filter(
            user1_id=user2_id, user2_id=user1_id).exists():
            return Response({"message": "Already friends."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            serializer.save()
            if FriendRequest.objects.filter(user1_id=user1_id,
                                            user2_id=user2_id).exists() and FriendRequest.objects.filter(
                user1_id=user2_id, user2_id=user1_id).exists():
                friends_serializer = FriendsPairSerializer(data={
                    'user1_id': user1_id,
                    'user2_id': user2_id
                })
                if friends_serializer.is_valid():
                    friends_serializer.save()
                FriendRequest.objects.filter(user1_id=user1_id, user2_id=user2_id).delete()
                FriendRequest.objects.filter(user1_id=user2_id, user2_id=user1_id).delete()
            return Response({"friend_request": serializer.data}, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def incoming_friend_requests(request, user_id):
    requests = FriendRequest.objects.filter(user2_id=user_id)
    return Response({"incoming friend requests": FriendRequestSerializer(requests, many=True).data})


@api_view(['GET'])
def outgoing_friend_requests(request, user_id):
    requests = FriendRequest.objects.filter(user1_id=user_id)
    return Response({"outgoing friend requests": FriendRequestSerializer(requests, many=True).data})


@api_view(['GET'])
def friends_list(request, user_id):
    friend_pairs = FriendsPair.objects.filter(Q(user1_id=user_id) | Q(user2_id=user_id))
    friends_list = [pair.user2_id if pair.user1_id == user_id else pair.user1_id for pair in friend_pairs]
    return Response({f"{user_id} friends ids": friends_list})


@api_view(['GET'])
def friend_status(request, user1_id, user2_id):
    friends_flag = FriendsPair.objects.filter(
        Q(user1_id=user1_id, user2_id=user2_id) | Q(user2_id=user1_id, user1_id=user2_id)).exists()
    incoming_flag = FriendRequest.objects.filter(user1_id=user2_id)
    outgoing_flag = FriendRequest.objects.filter(user1_id=user1_id)
    status_dict = {"status": "nothing"}
    if friends_flag:
        status_dict["status"] = "friends"
    elif incoming_flag:
        status_dict["status"] = "incoming friend request"
    elif outgoing_flag:
        status_dict["status"] = "outgoing friend request"
    return Response(status_dict)


@api_view(['DELETE'])
def delete_friend(request, user1_id, user2_id):
    friend_pair = FriendsPair.objects.filter(
        Q(user1_id=user1_id, user2_id=user2_id) | Q(user2_id=user1_id, user1_id=user2_id))
    if friend_pair:
        friend_pair.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response({"message": "not friends"}, status=status.HTTP_400_BAD_REQUEST)
