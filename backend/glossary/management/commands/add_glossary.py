from django.core.management import BaseCommand, CommandError
from glossary.models import GlossaryCategory, GlossaryTerm
import json

class Command(BaseCommand):
    def handle(self, *args, **options):
        file_path = '_data/glossary/all_glossary.json'

        with open(file_path, 'r', encoding="UTF-8") as f:
            data = json.load(f)

        for glossary in data:
            glossary_category_name = glossary['glossary_category_name']
            glossary_category_slug = glossary['glossary_category_slug']
            glossary_short_name = glossary['glossary_short_name']
            glossary_long_name = glossary['glossary_long_name']
            glossary_slug = glossary['glossary_slug']
            glossary_image_url = glossary['glossary_image_url']
            glossary_image_path = glossary['glossary_image_path']
            glossary_description = glossary['glossary_description']
            glossary_detail_url = glossary['glossary_detail_url']
            glossary_source_site = glossary['glossary_source_site']

            # Translation fields
            # glossary_description_de = glossary['glossary_description_de']

            if glossary_image_path is not None:
                image = f'glossary/{glossary_image_path}'
            else:
                image = None

            # Category
            try:
                category = GlossaryCategory.objects.get(slug=glossary_category_slug)
            except GlossaryCategory.DoesNotExist:
                category = GlossaryCategory(name=glossary_category_name, slug=glossary_category_slug)
                category.save()

            # short_name null
            # image_url null
            # image_path null

            try:
                term = GlossaryTerm(
                    short_name=glossary_short_name,
                    long_name=glossary_long_name,
                    slug=glossary_slug,
                    category=category,
                    image=image,
                    image_url=glossary_image_url,
                    image_path=glossary_image_path,
                    detail_url=glossary_detail_url,
                    source_site=glossary_source_site,
                    description=glossary_description
                )
                
                term.save()
                self.stdout.write(self.style.SUCCESS(f'{glossary_long_name} create successfully'))
            except Exception as e:
                raise CommandError(f'{e}')
