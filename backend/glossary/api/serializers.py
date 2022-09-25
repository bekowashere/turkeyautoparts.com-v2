from rest_framework import serializers
from glossary.models import GlossaryCategory, GlossaryTerm
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField

# ! GLOSSARY
class GlossaryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GlossaryCategory
        fields = '__all__'

class GlossaryTermSerializer(TranslatableModelSerializer):
    category = GlossaryCategorySerializer()

    translations = TranslatedFieldsField(shared_model=GlossaryTerm)

    class Meta:
        model = GlossaryTerm
        fields = (
            'short_name',
            'long_name',
            'slug',
            'category',
            'image',
            'image_url',
            'image_path',
            'detail_url',
            'source_site',
            'translations'
        )