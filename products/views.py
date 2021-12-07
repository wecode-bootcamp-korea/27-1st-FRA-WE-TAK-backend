from django.http.response  import JsonResponse
from django.views          import View

from products.models       import Product

class ProductListView(View):
    # :8000/products?offset=0&limit=100
    # :8000/products?offset=100&limit=100
    # :8000/products?offset=200&limit=100
    def get(self, request):
        offset   = request.GET.get("offset", 1)
        limit    = request.GET.get("limit", 100)
        products = Product.objects.all()[offset:offset+limit]

        results =[{
            'id'                 : product.id,
            'kr_name'            : product.kr_name,
            'en_name'            : product.en_name,
            'price'              : product.price,
            'sub_category_id'    : product.sub_category.id,
            'sub_category_name'  : product.sub_category.kr_name,
            'main_category_name' : product.sub_category.main_category.name,
            'main_category_id'   : product.sub_category.main_category.id,
            'rating'             : product.rating
            'images'             : [{
                "id"  :  image.id,
                "url" : image.url,
            } for image in product.image_set.all()],
        } for product in products]
        
        return JsonResponse({"result":results}, status=200)
