from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class FriendRequest(models.Model):
    user1_id = models.IntegerField()
    user2_id = models.IntegerField()

    def __str__(self):
        return f"{self.user1_id} -> {self.user2_id}"


class FriendsPair(models.Model):
    user1_id = models.IntegerField()
    user2_id = models.IntegerField()

    def __str__(self):
        return f"({self.user1_id}, {self.user2_id})"
