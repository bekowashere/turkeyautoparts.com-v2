from django.core.management import BaseCommand, CommandError
from autopart.models import Product, Manufacturer, CarBrand
from account.models import SupplierUser
from world.models import Currency
import json

class Command(BaseCommand):
    def handle(self, *args, **options):
        file_path = '_data/autopart/all_products.json'

        with open(file_path, 'r', encoding="UTF-8") as f:
            data = json.load(f)

        for product in data:
            supplier_company_name = product['supplier']
            oem_code = product['oem_code']
            manufacturer_no = product['manufacturer_code']
            product_image_url = product['product_image_url']
            manufacturer_name = product['manufacturer']
            car_brand_name = product['car_brand']
            # description = product['description']

            _currency = product['currency']
            currency_price = product['currency_price']
            supplier_net_price = product['kdv_net_price_lira']
            supplier_iskonto = product['iskonto']

            # CURRENCY
            if _currency == "€":
                try:
                    currency = Currency.objects.get(currency_code="EUR")
                except Currency.DoesNotExist:
                    print(f'Currency bulunamadı: {_currency}')
                    currency = None
            elif _currency == "$":
                try:
                    currency = Currency.objects.get(currency_code="USD")
                except Currency.DoesNotExist:
                    print(f'Currency bulunamadı: {_currency}')
                    currency = None
            elif _currency == "₺":
                try:
                    currency = Currency.objects.get(currency_code="TRY")
                except Currency.DoesNotExist:
                    print(f'Currency bulunamadı: {_currency}')
                    currency = None

            # %10 profit margin
            price_net = supplier_net_price + (supplier_net_price * 10 / 100)




            if manufacturer_name is not None:
                try:
                    manufacturer = Manufacturer.objects.get(name=manufacturer_name)
                except Manufacturer.DoesNotExist:
                    print(f'Manufacturer bulunamadı {manufacturer_name}')
                    manufacturer = None

            if car_brand_name is not None:
                try:
                    car_brand = CarBrand.objects.get(name=car_brand_name)
                except CarBrand.DoesNotExist:
                    print(f'Brand bulunamadı {car_brand_name}')
                    car_brand = None

            if supplier_company_name is not None:
                try:
                    supplier = SupplierUser.objects.get(company_name=supplier_company_name)
                except SupplierUser.DoesNotExist:
                    print(f'Supplier bulunamadı {supplier_company_name}')
                    supplier = None

            try:
                product = Product(
                    manufacturer=manufacturer,
                    car_brand=car_brand,
                    supplier=supplier,
                    oem_code = oem_code,
                    manufacturer_no=manufacturer_no,
                    product_image_url=product_image_url,
                    currency=currency,
                    currency_price=currency_price,
                    supplier_net_price=supplier_net_price,
                    supplier_iskonto=supplier_iskonto,
                    price_net=price_net
                )

                product.save()

                self.stdout.write(self.style.SUCCESS(f'{oem_code} create successfully'))
            except Exception as e:
                raise CommandError(f'{e}')