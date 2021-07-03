from django.db import models


class list(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item


class Work_Volume(models.Model):
    Tx_Name = models.CharField(max_length=200)
    Is_Active = models.BooleanField(default=True)

    def __str__(self):
        return self.Tx_Name
