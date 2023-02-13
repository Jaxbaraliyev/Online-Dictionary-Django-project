from django.db import models


class Lugat(models.Model):
    inglizcha = models.CharField('Inglizcha', max_length=100)
    uzbekcha = models.CharField('O`zbekcha', max_length=100)

    def __str__(self):
        return self.inglizcha
