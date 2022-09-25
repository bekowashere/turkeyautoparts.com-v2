from rest_framework.pagination import PageNumberPagination

class ProductPagination(PageNumberPagination):
    page_size = 20

class ManufacturerPagination(PageNumberPagination):
    page_size = 30

class CarBrandPagination(PageNumberPagination):
    page_size = 30