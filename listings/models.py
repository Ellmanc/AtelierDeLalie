from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Article(models.Model):
    name = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1500)
    stock = models.fields.IntegerField()
    price = models.fields.DecimalField(decimal_places=2,max_digits=5)

class New(models.Model):
    title = models.fields.CharField(max_length=100)
    content = models.fields.CharField(max_length=1500)
    field_name = models.ImageField(upload_to='')
    backImage = models.ImageField(upload_to='')


    def __str__(self):
        return f'{self.title}'
