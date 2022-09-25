from django.core.management import BaseCommand, CommandError
from auto.models import Brand
import json

class Command(BaseCommand):
    def handle(self, *args, **options):
        file_path = '_data/auto/all_brands.json'

        with open(file_path, 'r', encoding="UTF-8") as f:
            data = json.load(f)

        for brand in data:
            brand_name = brand['brand_name']
            brand_slug = brand['brand_slug']
            brand_detail_url = brand['brand_detail_url']
            brand_image_url = brand['brand_image_url']
            brand_image_path = brand['brand_image_path']
            image = f'auto/brands_logo/{brand_image_path}'

            # URL
            brand_detail_url_en = brand['brand_detail_url_en']
            brand_detail_url_de = brand['brand_detail_url_de']
            brand_detail_url_fr = brand['brand_detail_url_fr']

            # Translations fields
            brand_description_en = brand['brand_description_en']
            brand_description_de = brand['brand_description_de']
            brand_description_fr = brand['brand_description_fr']

            try:
                brand = Brand(
                    brand_name=brand_name,
                    brand_slug=brand_slug,
                    brand_image=image,
                    brand_image_url=brand_image_url,
                    brand_detail_url = brand_detail_url,
                    brand_detail_url_en = brand_detail_url_en,
                    brand_detail_url_de = brand_detail_url_de,
                    brand_detail_url_fr = brand_detail_url_fr,
                    brand_description = brand_description_en
                )
                

                brand.set_current_language('de')
                brand.brand_description = brand_description_de

                brand.set_current_language('fr')
                brand.brand_description = brand_description_fr

                brand.save()

                self.stdout.write(self.style.SUCCESS(f'{brand_name} create successfully'))
            except Exception as e:
                raise CommandError(f'{e}')