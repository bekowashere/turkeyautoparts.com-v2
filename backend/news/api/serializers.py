from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField
from news.models import Category, Tag, NewsItem
from account.models import User

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


# ! NEWS
class NewsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class NewsItemListSerializer(serializers.ModelSerializer):
    # user, category ve tags list olarak gözükmesede filtrelenebiliyor [kaldırdık]

    title_de = serializers.SerializerMethodField()
    title_fr = serializers.SerializerMethodField()
    title_en = serializers.SerializerMethodField()

    summary_text_de = serializers.SerializerMethodField()
    summary_text_fr = serializers.SerializerMethodField()
    summary_text_en = serializers.SerializerMethodField()

    category = CategoriesSerializer()
    tags = TagsSerializer(many=True)
    

    def get_title_de(self, obj):
        return obj.title_de

    def get_title_fr(self, obj):
        return obj.title_fr

    def get_title_en(self, obj):
        return obj.title_en
   
    class Meta:
        model = NewsItem
        fields = (
            'id',
            'slug',
            'title_en',
            'title_de',
            'title_fr',
            'summary_text_en',
            'summary_text_de',
            'summary_text_fr',
            'image',
            'status',
            'category',
            'tags',
            'created_date',
        )


class NewsItemDetailSerializer(TranslatableModelSerializer):
    user = NewsUserSerializer()
    category = CategoriesSerializer()
    tags = TagsSerializer(many=True)

    translations = TranslatedFieldsField(shared_model=NewsItem)

    class Meta:
        model = NewsItem
        fields = (
            'id',
            'user',
            'image',
            'category',
            'tags',
            'translations',
            'status',
            'created_date',
            'updated_date',
        )