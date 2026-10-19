
from django.db import models


class Vocabulary(models.Model):
    word = models.CharField(max_length=50)
    pinyin = models.CharField(max_length=100)
    meaning_ar = models.CharField(max_length=200)
    hsk_level = models.PositiveIntegerField()
    example = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.word