from django.db import models


class Chip(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    company = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "snack management"

    def __str__(self):
        return self.name
