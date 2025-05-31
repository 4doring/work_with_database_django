import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            record = Phone(
                name=phone['name'],
                image=phone['image'],
                price=int(phone['price']),
                release_date=datetime.strptime(phone['release_date'], "%Y-%m-%d"),
                lte_exists=phone['lte_exists'].lower() in ('true',),
                slug=slugify(phone['name']),
                )
            record.save()
