from django.db import models


class CarMake(models.Model):
    name = models.CharField(max_length=80, unique=True)
    country_of_origin = models.CharField(max_length=80, default='United States')

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=80)
    year = models.PositiveIntegerField(default=2026)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['car_make', 'name'], name='unique_car_model')]

    def __str__(self):
        return f'{self.car_make.name} {self.name}'
