from django.db import models

class sdata(models.Model):
    name = models.CharField(max_length = 100)
    dept = models.CharField(max_length = 100)     # dropdown of depts
    sap = models.IntegerField()
    source = models.CharField(max_length = 100)   #dropdown if possible
    type = models.IntegerField()          #dropdown only 1 or 2
    destination = models.CharField(max_length = 100)      #dropdown only vile parle
    issued = models.IntegerField()
    issuem = models.IntegerField()

    def __str__(self):
        return str(self.sap) + " - " + self.name
