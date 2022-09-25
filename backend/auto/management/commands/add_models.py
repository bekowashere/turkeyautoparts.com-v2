from django.core.management import BaseCommand, CommandError
from auto.models import Brand, Series, Model, FuelType, Segment, Infotainment, ModelImages
import json


class Command(BaseCommand):
    def handle(self, *args, **options):
        file_path = '_data/auto/all_models.json'

        with open(file_path, 'r', encoding="UTF-8") as f:
            data = json.load(f)

        for _model in data:
            brand_name = _model['brand_name']
            brand_detail_url = _model['brand_detail_url']
            brand_slug = _model['brand_slug']
            
            series_name = _model['series_name']
            # 1500/1600
            if '/' in series_name:
                series_name = series_name.replace('/','-')


            series_detail_url = _model['series_detail_url']
            series_slug = _model['series_slug']

            model_name = _model['model_name']
            model_detail_url = _model['model_detail_url']
            model_slug = _model['model_slug']

            model_image_url = _model['model_image_url']
            model_image_path = _model['model_image_path']

            _model_start_year = _model['model_first_year']
            _model_end_year = _model['model_last_year']

            
            _model_segment = _model['model_segment']
            # Body Style CharField (for Model)
            model_bodyStyle = _model['model_bodyStyle']

            # URL
            model_detail_url_en = _model['model_detail_url_en']
            model_detail_url_de = _model['model_detail_url_de']
            model_detail_url_fr = _model['model_detail_url_fr']

            # Translations fields
            model_description_en = _model['model_description_en']
            model_description_de = _model['model_description_de']
            model_description_fr = _model['model_description_fr']

            image = f'auto/{brand_name}/{series_name}/{model_image_path}'

            # brand_detail_url is UNIQUE
            brand = Brand.objects.get(brand_detail_url=brand_detail_url)
            # series_detail_url is UNIQUE
            series = Series.objects.get(series_detail_url=series_detail_url)

            # Segment FK
            if _model_segment is not None:
                try:
                    model_segment = Segment.objects.get(name=_model_segment)
                except Segment.DoesNotExist:
                    model_segment = Segment(name=_model_segment)
                    model_segment.save()

            # Year convert Integer
            model_start_year = int(_model_start_year)
            if _model_end_year == "Present":
                model_end_year = 2022
            else:
                model_end_year = int(_model_end_year)

            try:
                model = Model(
                    model_brand=brand,
                    model_series=series,
                    model_name=model_name,
                    model_slug=model_slug,
                    model_image=image,
                    model_image_url=model_image_url,
                    model_image_path=model_image_path,
                    model_start_year=model_start_year,
                    model_end_year=model_end_year,
                    model_segment=model_segment,
                    model_bodyStyle=model_bodyStyle,
                    model_detail_url=model_detail_url,
                    model_detail_url_en=model_detail_url_en,
                    model_detail_url_de=model_detail_url_de,
                    model_detail_url_fr=model_detail_url_fr,
                    model_description=model_description_en      
                )

                # DESCRIPTION
                model.set_current_language('de')
                model.model_description = model_description_de

                model.set_current_language('fr')
                model.model_description = model_description_fr
                model.save()

                # model_infotainment
                infotainments = _model['model_infotainment']
                if len(infotainments) > 0:
                    for infot in infotainments:
                        try:
                            infotainment = Infotainment.objects.get(name=infot)
                        except Infotainment.DoesNotExist:
                            infotainment = Infotainment(name=infot)
                            infotainment.save()
                        model.model_infotainment.add(infotainment)
                model.save()
                
                # model_fuelType
                fuelTypes = _model['model_fuelType']
                if len(fuelTypes) > 0:
                    for fuel in fuelTypes:
                        try:
                            fueltype = FuelType.objects.get(type=fuel)
                        except FuelType.DoesNotExist:
                            fueltype = FuelType(type=fuel)
                            fueltype.save()
                        model.model_fuelType.add(fueltype)
                model.save()

                # MODEL IMAGES CREATE
                model_images_url = _model['model_images_url']
                if len(model_images_url) > 0:
                    for img_url in model_images_url:
                        txt1, image_alt_text = model_image_url.rsplit('/', 1)
                        ModelImages.objects.create(
                            model=model,
                            image_url=img_url,
                            alt_text=image_alt_text
                        )

                self.stdout.write(self.style.SUCCESS(f'{model_name} create successfully'))
            except Exception as e:
                raise CommandError(f'{e}')


            