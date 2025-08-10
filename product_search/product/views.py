from django.shortcuts import render
from product.models.category import Category
from product.models.product import Product
from product.models.tag import Tag 

def product_list(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')
    tag_ids = request.GET.getlist('tags')

    products = Product.objects.all()

    if query:
        products = products.filter(description__icontains=query)
    if category_id:
        category = Category.objects.get(id=category_id)
        descendant_ids = [category.id] + [desc.id for desc in category.get_descendants()]
        products = products.filter(category__id__in=descendant_ids)
    if tag_ids:
        products = products.filter(tags__id__in=tag_ids).distinct()
    
    context = {
        'products': products,
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
        'selected_category': category_id,
        'selected_tags': tag_ids,
        'query': query
    }
    
    return render(request, 'product/product_list.html', context)