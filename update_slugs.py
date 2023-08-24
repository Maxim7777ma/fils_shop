import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")
django.setup()

from django.utils.text import slugify
from app.models import Film

films = Film.objects.all()

for film in films:
    film.slug = slugify(film.label)
    film.save()

print("Slugs updated successfully.")