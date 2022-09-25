### START GUIDE

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
```

### ACCOUNT

```
python manage.py add_supplier [email] [password] [company_name] [code]
python manage.py add_supplier mercanlar@gmail.com Berke1919*- Mercanlar MERC

python manage.py add_customer [email] [first_name] [last_name] [password]
python manage.py add_customer customer@gmail.com Berke Karataş BerkeB1919*-
```

### WORLD

```
python manage.py add_countries
```

### AUTO

```
python manage.py add_brands
python manage.py add_series
python manage.py add_models
python manage.py add_specification_types
python manage.py add_specifications
python manage.py add_cars
```

### AUTOPART

```
python manage.py add_manufacturers
python manage.py add_car_brands
python manage.py add_products
```

### GLOSSARY

```
python manage.py add_glossary
```

### CLEAR PYCACHE - MIGRATIONS

```
clear.sh
```

### CLEAR BASH COMMANDS

```
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete
find . -path "**/__pycache__/*"  -delete
find . -path "**/__pycache__"  -delete
```

