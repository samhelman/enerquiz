from django.db import models

class Result(models.Model):
    result = models.IntegerField()

    def __str__(self):
        return str(self.result)