from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify

class Ganre(models.Model):
    ganre = models.CharField(max_length=23)
    avarage_rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.ganre}, {self.avarage_rating}"

class Actor(models.Model):
    name = models.CharField(max_length=23)
    surname = models.CharField(max_length=23)

    def __str__(self):
        return f"{self.surname}, {self.name}"

class Producer(models.Model):
    name = models.CharField(max_length=23)
    surname = models.CharField(max_length=23)
    
    def __str__(self):
        return f"{self.surname}, {self.name}"

class Film(models.Model):
    label = models.CharField(max_length=23, default="Unknown Film", null=False)
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    image = models.CharField(max_length=200)
    producer = models.ForeignKey(Producer, on_delete=models.PROTECT)
    actors = models.ManyToManyField(Actor)
    ganre = models.ForeignKey(Ganre, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.label)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.label