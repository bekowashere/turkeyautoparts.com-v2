from django.core.management import BaseCommand, CommandError
from autopart.models import CarBrand

import json

class Command(BaseCommand):
    def handle(self, *args, **options):
        file_path = '_data/autopart/all_car_brands.json'

        with open(file_path, 'r', encoding="UTF-8") as f:
            data = json.load(f)

        for cab in data:
            name = cab['name']
            slug = cab['slug']
            code = cab['code']
            image_path = cab['image_path']

            if image_path is not None:
                image = f'autopart/CarBrand/{image_path}'
            else:
                image = f'autopart/default.png'
            
            try:
                car_brand = CarBrand(
                    name=name,
                    slug=slug,
                    code=code,
                    image=image
                )

                car_brand.save()

                self.stdout.write(self.style.SUCCESS(f'{name} create successfully'))
            except Exception as e:
                raise CommandError(f'{e}')