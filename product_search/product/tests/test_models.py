from django.test import TestCase
from product.models.category import Category
from product.models.product import Product
from product.models.tag import Tag

class TestCategoryModel(TestCase):
    def test_create_category(self):
        parent = Category.objects.create(name="Electronics")
        child = Category.objects.create(name="Laptops", parent=parent)
        self.assertEqual(child.parent, parent)
        self.assertEqual(str(child), "Laptops")

    def test_get_descendants(self):
        root = Category.objects.create(name="computer")
        child = Category.objects.create(name="laptop", parent=root)
        grandchild = Category.objects.create(name="macbook", parent=child)
        descendants = root.get_descendants()
        self.assertIn(child, descendants)
        self.assertIn(grandchild, descendants)

class TestProductModel(TestCase):
    def test_create_product_with_tags_and_category(self):
        category = Category.objects.create(name="Electronics")
        tag1 = Tag.objects.create(name="camera")
        tag2 = Tag.objects.create(name="latest")
        product = Product.objects.create(name="Camera X", category=category)
        product.tags.add(tag1, tag2)
        self.assertEqual(product.category, category)
        self.assertIn(tag1, product.tags.all())
        self.assertIn(tag2, product.tags.all())
        self.assertEqual(str(product), "Camera X")

class TestTagModel(TestCase):
    def test_create_tag(self):
        tag = Tag.objects.create(name="electronics")
        self.assertEqual(str(tag), "electronics")
