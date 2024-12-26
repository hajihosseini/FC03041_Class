from django.db import models


class Contacts(models.Model) :
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    number = models.IntegerField()
    sen = models.IntegerField()


    def __str__(self):
        return f"user:{self.firstname} {self.lastname} - {self.number}"