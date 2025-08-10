from django.core.management.base import BaseCommand
from product.models.category import Category
from product.models.product import Product
from product.models.tag import Tag 

class Command(BaseCommand):
    help = 'Populate the database with initial data.'

    def delete_everything(self):
        Product.objects.all().delete()
        Category.objects.all().delete()
        Tag.objects.all().delete()

    def handle(self, *args, **options):
        # Delete existing data
        self.delete_everything()
        
        # Add tags
        tag_names = [
            'on clearance', 
            'refurbished', 
            'online only', 
            'back to school sale', 
            'latest and greatest', 
            'lightweight'
        ]
        tags = []
        for name in tag_names:
            tag, _ = Tag.objects.get_or_create(name=name)
            tags.append(tag)

        # Add categories
        class CategoryParent:
            def __init__(self, name, parent=None):
                self.name = name
                self.parent = parent

        category_names = [
            CategoryParent('Computers', None),
            CategoryParent('Laptops', 'Computers'),
            CategoryParent('Desktops', 'Computers'),
            CategoryParent('Windows Laptops', 'Laptops'),
            CategoryParent('MacBooks', 'Laptops'),
            CategoryParent('PCs', 'Desktops'),
            CategoryParent('IMac', 'Desktops')
        ]

        for categorys in category_names:
            if categorys.parent:
                parent_obj, _ = Category.objects.get_or_create(
                    name=categorys.parent
                )
            else:
                parent_obj = None
            category, _ = Category.objects.get_or_create(
                name=categorys.name,
                parent=parent_obj
            )

        # Add products
        products = [
            {
                'name': 'ASUS Vivobook 16',
                'description': 'ASUS Vivobook 16',
                'category': 'PCs',
                'tags': ['on clearance', 'refurbished']
            },
            {
                'name': 'ASUS ROG Zephyrus G14',
                'description': 'ASUS ROG Zephyrus G14',
                'category': 'PCs',
                'tags': ['online only', 'latest and greatest']
            },
            {
                'name': 'Apple IMac',
                'description': 'Apple IMac',
                'category': 'IMac',
                'tags': ['back to school sale', 'latest and greatest']
            },
            {
                'name': 'Apple MacBook Air',
                'description': 'Apple MacBook Air',
                'category': 'MacBooks',
                'tags': ['on clearance', 'latest and greatest']
            },
            {
                'name': 'Apple MacBook Pro',
                'description': 'Apple MacBook Pro',
                'category': 'MacBooks',
                'tags': ['online only', 'latest and greatest']
            },
            {
                'name': 'HP Elite Dragonfly',
                'description': 'HP Elite Dragonfly',
                'category': 'Windows Laptops',
                'tags': ['on clearance', 'latest and greatest']
            },
            {
                'name': 'Apple MacBook Pro',
                'description': 'Apple MacBook Pro',
                'category': 'Windows Laptops',
                'tags': ['online only', 'latest and greatest']
            },
            {
                'name': 'Dell XPS 13',
                'description': 'Dell XPS 13 Ultrabook',
                'category': 'Windows Laptops',
                'tags': ['online only', 'refurbished']
            },
            {
                'name': 'Lenovo ThinkPad X1 Carbon',
                'description': 'Lenovo ThinkPad X1 Carbon',
                'category': 'Windows Laptops',
                'tags': ['latest and greatest', 'back to school sale']
            },
            {
                'name': 'Microsoft Surface Laptop 5',
                'description': 'Microsoft Surface Laptop 5',
                'category': 'Windows Laptops',
                'tags': ['back to school sale', 'online only']
            },
            {
                'name': 'Acer Aspire 5',
                'description': 'Acer Aspire 5 Slim Laptop',
                'category': 'Windows Laptops',
                'tags': ['on clearance', 'back to school sale']
            },
            {
                'name': 'HP Pavilion Desktop',
                'description': 'HP Pavilion Desktop Computer',
                'category': 'PCs',
                'tags': ['refurbished', 'online only']
            },
            {
                'name': 'Apple IMac Mini',
                'description': 'Apple Mac Mini Desktop',
                'category': 'IMac',
                'tags': ['latest and greatest', 'back to school sale']
            },
            {
                'name': 'Alienware Aurora R13',
                'description': 'Alienware Aurora R13 Gaming Desktop',
                'category': 'PCs',
                'tags': ['on clearance', 'latest and greatest']
            },
            {
                'name': 'Samsung Galaxy Book Pro',
                'description': 'Samsung Galaxy Book Pro Laptop',
                'category': 'Windows Laptops',
                'tags': ['online only', 'latest and greatest']
            },
            {
                'name': 'Razer Blade 15',
                'description': 'Razer Blade 15 Gaming Laptop',
                'category': 'Windows Laptops',
                'tags': ['on clearance', 'latest and greatest']
            },
            {
                'name': 'Apple MacBook Pro M2',
                'description': 'Apple MacBook Pro M2',
                'category': 'MacBooks',
                'tags': ['latest and greatest', 'online only']
            },
            {
                'name': 'Google Pixelbook Go',
                'description': 'Google Pixelbook Go Chromebook',
                'category': 'Windows Laptops',
                'tags': ['online only', 'back to school sale']
            },
            {
                'name': 'MSI Stealth 15M',
                'description': 'MSI Stealth 15M Gaming Laptop',
                'category': 'Windows Laptops',
                'tags': ['on clearance', 'latest and greatest']
            },
            {
                'name': 'LG Gram 17',
                'description': 'LG Gram 17 Ultra-lightweight Laptop',
                'category': 'Windows Laptops',
                'tags': ['lightweight', 'latest and greatest']
            }
        ]
        for product_input in products:
            product_name = product_input['name']
            description = product_input['description']
            category = Category.objects.get(name=product_input['category'])
            product, _ = Product.objects.get_or_create(
                name=product_name,
                description=description,
                category=category
            )
            product.tags.set([Tag.objects.get(name=tag) for tag in product_input['tags']])
            product.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated initial data.'))
