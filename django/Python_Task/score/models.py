from django.db import models

from core.models import BaseModel


class Restaurant(BaseModel):
    name = models.CharField(max_length=50)
    kitchen_type = models.CharField(max_length=20)

    class Meta:
        db_table = 'restaurant'

    def __str__(self):
        return f'{self.name} {self.kitchen_type}'


class Vote(BaseModel):
    vote = models.PositiveIntegerField(null=True, blank=True)
    employee = models.OneToOneField(
        'score.Menu',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='employee')

    def __str__(self):
        return f'{self.vote}'

    class Meta:
        db_table = 'vote'


class Menu(BaseModel):
    menu = models.CharField(max_length=200)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant')
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, related_name='score', null=True, blank=True)

    class Meta:
        db_table = 'menu'

    def __str__(self):
        return f'{self.menu}'


class Employee(BaseModel):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Scores(BaseModel):
    voter = models.OneToOneField(
        'score.Employee',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='voter_field')
    score = models.OneToOneField(
        'score.Vote',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='score_field')
    menu = models.OneToOneField(
        'score.Menu',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='menu_field')

    def __str__(self):
        return f'{self.voter} {self.score} {self.menu}'


