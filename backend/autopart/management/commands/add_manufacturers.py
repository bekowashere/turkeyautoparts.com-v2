from django.core.management import BaseCommand, CommandError
from autopart.models import Manufacturer

import json

class Command(BaseCommand):
    def handle(self, *args, **options):
        file_path = '_data/autopart/all_manufacturers.json'

        with open(file_path, 'r', encoding="UTF-8") as f:
            data = json.load(f)

        for man in data:
            name = man['name']
            slug = man['slug']
            code = man['code']
            image_path = man['image_path']

            if image_path is not None:
                image = f'autopart/Manufacturer/{image_path}'
            else:
                image = f'autopart/default.png'
            
            try:
                manufacturer = Manufacturer(
                    name=name,
                    slug=slug,
                    code=code,
                    image=image
                )

                manufacturer.save()

                self.stdout.write(self.style.SUCCESS(f'{name} create successfully'))
            except Exception as e:
                raise CommandError(f'{e}')