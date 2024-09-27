from django.db import models

DEFAULT_STAT_VALUE = 2
ANIMAL_STAT_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)
CHARACTER_COMPLEXITY_CHOICES = (
    ("easy", "Easy"),
    ("medium", "Medium"),
    ("hard", "Hard"),
)


class Animal(models.Model):
    """Dale of Merchants Animal model"""
    name = models.CharField(max_length=50, unique=True)
    complexity = models.PositiveIntegerField(
        default=DEFAULT_STAT_VALUE,
        choices=ANIMAL_STAT_CHOICES
    )
    interactivity = models.PositiveIntegerField(
        default=DEFAULT_STAT_VALUE,
        choices=ANIMAL_STAT_CHOICES
    )
    nastiness = models.PositiveIntegerField(
        default=DEFAULT_STAT_VALUE,
        choices=ANIMAL_STAT_CHOICES
    )
    randomness = models.PositiveIntegerField(
        default=DEFAULT_STAT_VALUE,
        choices=ANIMAL_STAT_CHOICES
    )

    def __str__(self):
        return f"{self.name}"


class Character(models.Model):
    """Dale of Merchants Character model"""
    name = models.CharField(max_length=50, unique=True)
    complexity = models.CharField(
        max_length=10,
        choices=CHARACTER_COMPLEXITY_CHOICES,
        default="easy"
    )

    def __str__(self):
        return f"Character {self.name}"
