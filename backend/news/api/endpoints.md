# news API endpoints
***
**endpoint:** api/news/list/

**method:** GET

**serializer:** NewsItemListSerializer

**view:** NewsItemListAPIView

**filterset_fields:** ['tags__slug', 'category__slug', 'user__username']

**example_url:** http://127.0.0.1:8000/api/news/list/?tags__slug=bmw&category__slug=renderings


## JSON
```
...
```
***
**endpoint:** api/news/detail/<slug>/

**method:** GET

**serializer:** NewsItemDetailSerializer

**view:** NewsItemDetailAPIView


## JSON
```
...
```