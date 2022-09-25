from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField
from auto.models import (
    Brand,
    Series,
    Model,
    Car,
    CarSpecificationValue,
    FuelType,
    Infotainment,
    Segment,
    BodyStyle,
    ModelImages
)

# ! HELPERS
class FuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelType
        fields = ('id','type',)

class InfotainmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infotainment
        fields = ('id', 'name', 'icon')


class CarSerializer(serializers.ModelSerializer):
    car_brand_name = serializers.SerializerMethodField()
    car_series_name = serializers.SerializerMethodField()
    car_model_name = serializers.SerializerMethodField()

    def get_car_brand_name(self, obj):
        return obj.car_brand.brand_name

    def get_car_series_name(self, obj):
        return obj.car_series.series_name

    def get_car_model_name(self, obj):
        return obj.car_model.model_name

    class Meta:
        model = Car
        fields = (
            'id',
            'car_brand_name',
            'car_series_name',
            'car_model_name',
            'car_name',
            'car_slug',
            'car_fuelType',
            'car_driveType',
            'car_gearBox',
            'car_engine',
            'car_enginePower'
        )

class SummaryBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'brand_name', 'brand_slug', 'brand_image')

class SummarySeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ('id', 'series_name', 'series_slug', 'series_image')

class SummaryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ('id', 'model_name', 'model_slug', 'model_image')
    

# ! BRAND LIST - DETAIL :START
class BrandSomeSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ('id', 'series_name', 'series_slug')

class BrandListSerializer(TranslatableModelSerializer):
    brand_in_production_count = serializers.SerializerMethodField()
    brand_discontinued_count = serializers.SerializerMethodField()
    brand_some_series = serializers.SerializerMethodField()
    brand_url = serializers.HyperlinkedIdentityField(
        view_name='auto:brand_detail',
        lookup_field='brand_slug'
    )

    translations = TranslatedFieldsField(shared_model=Brand)

    def get_brand_in_production_count(self, obj):
        return obj.get_continued_count()

    def get_brand_discontinued_count(self, obj):
        return obj.get_discontinued_count()

    def get_brand_some_series(self, obj):
        return BrandSomeSeriesSerializer(obj.get_some_series, many=True).data

    class Meta:
        model = Brand
        fields = (
            'id',
            'brand_name',
            'brand_slug',
            'brand_url',
            'brand_detail_url',
            'brand_image',
            'brand_image_url',
            'brand_in_production_count',
            'brand_discontinued_count',
            'brand_some_series',
            'translations'
        )


class SeriesSerializer(serializers.ModelSerializer):
    series_bodyStyle = serializers.SerializerMethodField()
    series_fuelType = FuelTypeSerializer(many=True)
    series_generation_count = serializers.SerializerMethodField()
    series_generation_oldest_year = serializers.SerializerMethodField()
    series_generation_newest_year = serializers.SerializerMethodField()

    def get_series_bodyStyle(self, obj):
        return obj.series_bodyStyle.style

    def get_series_generation_count(self, obj):
        return obj.get_models_count()

    def get_series_generation_oldest_year(self, obj):
        return obj.get_first_year()

    def get_series_generation_newest_year(self, obj):
        return obj.get_last_year()

    class Meta:
        model = Series
        fields = (
            'id',
            'series_name',
            'series_slug',
            'series_image',
            'series_image_url',
            'series_bodyStyle',
            'series_fuelType',
            'series_isDiscontinued',
            'series_generation_count_bot',
            'series_generation_count',
            'series_generation_oldest_year',
            'series_generation_newest_year',
        )


class BrandDetailSerializer(TranslatableModelSerializer):
    brand_total_series_count = serializers.SerializerMethodField()
    brand_in_production_count = serializers.SerializerMethodField()
    brand_discontinued_count = serializers.SerializerMethodField()
    
    brand_continued_series = serializers.SerializerMethodField()
    brand_discontinued_series = serializers.SerializerMethodField()

    translations = TranslatedFieldsField(shared_model=Brand)

    def get_brand_total_series_count(self, obj):
        return obj.get_total_series_count()

    def get_brand_in_production_count(self, obj):
        return obj.get_continued_count()

    def get_brand_discontinued_count(self, obj):
        return obj.get_discontinued_count()

    def get_brand_continued_series(self, obj):
        return SeriesSerializer(obj.get_continued_series, many=True).data

    def get_brand_discontinued_series(self, obj):
        return SeriesSerializer(obj.get_discontinued_series, many=True).data

    class Meta:
        model = Brand
        fields = (
            'id',
            'brand_name',
            'brand_slug',
            'brand_image',
            'brand_image_url',

            'brand_total_series_count',
            'brand_in_production_count',
            'brand_discontinued_count',

            'brand_detail_url',
            'brand_detail_url_en',
            'brand_detail_url_de',
            'brand_detail_url_fr',

            'brand_continued_series',
            'brand_discontinued_series',
            'translations'
        )
# ! BRAND LIST - DETAIL :FINISH

# ! SERIES LIST - DETAIL :START
class SeriesModelSerializer(TranslatableModelSerializer):
    model_fuelType = FuelTypeSerializer(many=True)
    model_cars = serializers.SerializerMethodField()

    # EN - DE - FR HOW?
    translations = TranslatedFieldsField(shared_model=Model)

    # def get_model_description(self, obj):
    #     return obj.model_description[:200]

    def get_model_cars(self, obj):
        return CarSerializer(obj.get_all_cars, many=True).data
    
    class Meta:
        model = Model
        fields = (
            'id',
            'model_name',
            'model_slug',
            'model_image',
            'model_start_year',
            'model_end_year',
            'model_fuelType',
            'translations',
            'model_cars'
        )

class SeriesListSerializer(serializers.ModelSerializer):
    series_brand = SummaryBrandSerializer()
    series_fuelType = FuelTypeSerializer(many=True)

    series_bodyStyle = serializers.SerializerMethodField()
    series_generation_count = serializers.SerializerMethodField()
    series_generation_oldest_year = serializers.SerializerMethodField()
    series_generation_newest_year = serializers.SerializerMethodField()

    def get_series_bodyStyle(self, obj):
        return obj.series_bodyStyle.style

    def get_series_generation_count(self, obj):
        return obj.get_models_count()

    def get_series_generation_oldest_year(self, obj):
        return obj.get_first_year()

    def get_series_generation_newest_year(self, obj):
        return obj.get_last_year()

    class Meta:
        model = Series
        fields = (
        'series_brand',
        'id',
        'series_name',
        'series_slug',
        'series_image',
        'series_image_url',
        'series_bodyStyle',
        'series_fuelType',
        'series_isDiscontinued',
        'series_generation_count_bot',
        'series_generation_count',
        'series_generation_oldest_year',
        'series_generation_newest_year',
        'series_detail_url',
        )

class SeriesDetailSerializer(serializers.ModelSerializer):
    series_brand = SummaryBrandSerializer()
    series_fuelType = FuelTypeSerializer(many=True)

    series_first_production_year = serializers.SerializerMethodField()
    series_bodyStyle = serializers.SerializerMethodField()
    series_generation_count = serializers.SerializerMethodField()
    series_generation_oldest_year = serializers.SerializerMethodField()
    series_generation_newest_year = serializers.SerializerMethodField()
    series_models = serializers.SerializerMethodField()

    def get_series_first_production_year(self, obj):
        return obj.get_first_year()

    def get_series_bodyStyle(self, obj):
        return obj.series_bodyStyle.style

    def get_series_generation_count(self, obj):
        return obj.get_models_count()

    def get_series_generation_oldest_year(self, obj):
        return obj.get_first_year()

    def get_series_generation_newest_year(self, obj):
        return obj.get_last_year()

    def get_series_models(self, obj):
        return SeriesModelSerializer(obj.get_all_models, many=True).data

    class Meta:
        model = Series
        fields = (
        'series_brand',
        'id',
        'series_name',
        'series_slug',
        'series_image',
        'series_image_url',
        'series_first_production_year',
        'series_bodyStyle',
        'series_fuelType',
        'series_isDiscontinued',
        'series_generation_count_bot',
        'series_generation_count',
        'series_generation_oldest_year',
        'series_generation_newest_year',
        'series_detail_url',
        'series_models'
        )
# ! SERIES LIST - DETAIL :FINISH

# ! MODEL LIST - DETAIL :START
class ModelImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelImages
        fields = ('id', 'image_url', 'alt_text')

class ModelListSerializer(TranslatableModelSerializer):
    model_brand = SummaryBrandSerializer()
    model_series = SummarySeriesSerializer()
    model_fuelType = FuelTypeSerializer(many=True)
    model_infotainment = InfotainmentSerializer(many=True)
    model_segment = serializers.SerializerMethodField()
    model_cars = serializers.SerializerMethodField()

    translations = TranslatedFieldsField(shared_model=Model)

    def get_model_segment(self, obj):
        return obj.model_segment.name

    def get_model_cars(self, obj):
        return CarSerializer(obj.get_all_cars, many=True).data

    class Meta:
        model = Model
        fields = (
            'model_brand',
            'model_series',
            'id',
            'model_name',
            'model_slug',
            'model_image',
            'model_image_url',
            'model_image_path',
            'model_start_year',
            'model_end_year',
            'model_fuelType',
            'model_segment',
            'model_bodyStyle',
            'model_infotainment',
            'model_detail_url',
            'model_detail_url_en',
            'model_detail_url_de',
            'model_detail_url_fr',
            'translations',
            'model_cars'
        )

class ModelDetailSerializer(TranslatableModelSerializer):
    model_brand = SummaryBrandSerializer()
    model_series = SummarySeriesSerializer()
    model_fuelType = FuelTypeSerializer(many=True)
    model_infotainment = InfotainmentSerializer(many=True)
    model_segment = serializers.SerializerMethodField()
    model_cars = serializers.SerializerMethodField()
    model_images = serializers.SerializerMethodField()

    translations = TranslatedFieldsField(shared_model=Model)

    def get_model_segment(self, obj):
        return obj.model_segment.name

    def get_model_cars(self, obj):
        return CarSerializer(obj.get_all_cars, many=True).data

    def get_model_images(self, obj):
        return ModelImagesSerializer(obj.get_all_model_images, many=True).data

    class Meta:
        model = Model
        fields = (
            'model_brand',
            'model_series',
            'id',
            'model_name',
            'model_slug',
            'model_image',
            'model_image_url',
            'model_image_path',
            'model_start_year',
            'model_end_year',
            'model_fuelType',
            'model_segment',
            'model_bodyStyle',
            'model_infotainment',
            'model_detail_url',
            'model_detail_url_en',
            'model_detail_url_de',
            'model_detail_url_fr',
            'translations',
            'model_cars',
            'model_images'
        )
# ! MODEL LIST - DETAIL :FINISH

# ! CAR
class CarSpecificationValueSerializer(serializers.ModelSerializer):
    specification_type = serializers.SerializerMethodField()
    specification = serializers.SerializerMethodField()

    def get_specification_type(self, obj):
        return obj.specification.cs_type.name

    def get_specification(self, obj):
        return obj.specification.name

    class Meta:
        model = CarSpecificationValue
        fields = ('specification_type', 'specification', 'value')

class CarDetailSerializer(serializers.ModelSerializer):
    car_brand = SummaryBrandSerializer()
    car_series = SummarySeriesSerializer()
    car_model = SummaryModelSerializer()
    car_specifications = serializers.SerializerMethodField()

    def get_car_specifications(self, obj):
        return CarSpecificationValueSerializer(obj.get_all_specifications, many=True).data

    class Meta:
        model = Car
        fields = (
            'car_brand',
            'car_series',
            'car_model',
            'id',
            'car_name',
            'car_slug',
            'car_fuelType',
            'car_driveType',
            'car_gearBox',
            'car_engine',
            'car_enginePower',
            'car_detail_url',
            'car_alt_url',
            'car_specifications'
        )
