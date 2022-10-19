from django.db import models

from core.models import BaseModel


class Restaurant(BaseModel):
    name = models.CharField(max_length=50)
    kichen_type = models.CharField(max_length=20)

    class Meta:
        db_table = 'restaurant'

    def __str__(self):
        return f'{self.name} {self.kichen_type}'


class Menu(BaseModel):
    menu = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant')

    class Meta:
        db_table = 'Menu'

    def __str__(self):
        return f'{self.menu} {self.restaurant}'


class Employee(BaseModel):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'Employee'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
