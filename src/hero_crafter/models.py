from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class _AbilityScoreField(models.IntegerField):
    default_validators = [
        MinValueValidator(3), MaxValueValidator(18),
    ]


class Character(models.Model):
    name = models.CharField(max_length=100)

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    strength = _AbilityScoreField()
    intelligence = _AbilityScoreField()
    wisdom = _AbilityScoreField()
    dexterity = _AbilityScoreField()
    constitution = _AbilityScoreField()
    charisma = _AbilityScoreField()

    hit_points = models.IntegerField()

    RACE_CHOICES = [
        ('D', 'Dwarf'),
        ('E', 'Elf'),
        ('HL', 'Halfling'),
        ('H', 'Human'),
    ]
    race = models.CharField(max_length=2, choices=RACE_CHOICES)

    CLASS_CHOICES = [
        ('C', 'Cleric'),
        ('F', 'Fighter'),
        ('M', 'Mage'),
        ('T', 'Thief'),
    ]
    character_class = models.CharField(max_length=1, choices=CLASS_CHOICES, db_column='class')

    ALIGNMENT_CHOICES = [
        ('LG', 'Lawful Good'),
        ('NG', 'Neutral Good'),
        ('CG', 'Chaotic Good'),
        ('LN', 'Lawful Neutral'),
        ('TN', 'True Neutral'),
        ('CN', 'Chaotic Neutral'),
        ('LE', 'Lawful Evil'),
        ('NE', 'Neutral Evil'),
        ('CE', 'Chaotic Evil'),
    ]

    alignment = models.CharField(max_length=2, choices=ALIGNMENT_CHOICES)

    biography = models.TextField(blank=True, null=True)

    portrait_url = models.URLField(blank=True, null=True, max_length=1000)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='characters')
