from django.db import models


class GameSet(models.Model):
    """Unmatched Game Set model"""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name} Unmatched set"


class Character(models.Model):
    """Unmatched Character model"""
    name = models.CharField(max_length=50, unique=True)
    complexity = models.PositiveIntegerField()
    game_set = models.ForeignKey(GameSet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Map(models.Model):
    """Unmatched Map model"""
    name = models.CharField(max_length=50, unique=True)
    game_set = models.ForeignKey(GameSet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
