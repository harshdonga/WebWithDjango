from django.db import models

class auth(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

class cdata(models.Model):
    name = models.CharField(max_length = 100)
    dept = models.CharField(max_length = 100)
    sap = models.IntegerField()
    source = models.CharField(max_length = 100)
    previssued = models.IntegerField()
    previssuem = models.IntegerField()

    def __str__(self):
        return str(self.sap) + " - " + self.name

class validated(models.Model):
        name = models.CharField(max_length = 100)
        source = models.CharField(max_length = 100)
        destination = models.CharField(max_length=100)
        type = models.IntegerField()
        def __str__(self):
            return str(self.name)
