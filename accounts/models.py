from django.db import models


class UserAccounts(models.Model):
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    creationDate = models.DateTimeField(auto_now_add=True)
    #IDK WHAT THE FUCK IM DOING ATP ;/ help!
    def __str__(self):
        return f"USERNAME : {self.username} Created At {self.creationDate}"