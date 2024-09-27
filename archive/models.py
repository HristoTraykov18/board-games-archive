from django.db import models


class BoardGame(models.Model):
    """Board Games Archive Board Games Model"""
    name = models.CharField(max_length=100, unique=True)
    year = models.IntegerField()
    image = models.ImageField()
    link = models.URLField(max_length=200, unique=True)
    number_of_players = models.CharField(max_length=5)
    duration = models.CharField(max_length=10)
    complexity = models.FloatField(max_length=5)

    def __str__(self):
        return f"{self.name} ({self.year})"


class Player(models.Model):
    """Board Games Archive Player model"""
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class GameSession(models.Model):
    """Board Games Archive Game Session model"""
    board_game = models.OneToOneField(BoardGame, on_delete=models.CASCADE)
    players = models.ManyToManyField(Player)
    winner = models.OneToOneField(Player, null=True,
                                  related_name="winner",
                                  on_delete=models.SET_NULL)

    def __str__(self):
        return f"Session of {self.board_game} with a winner {self.winner}"
