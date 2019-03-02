from django.db import models

class auth(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    creds = models.IntegerField()

    def __str__(self):
        return self.username
