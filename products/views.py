import json

from django.http.response import JsonResponse
from django.views         import View

from .models              import Product

class SearchView(View):
    def get(self, request):
        data    = json.loads(request.body)
        products = Product.objects.filter(kr_name = data['search'])
        for product in products:
            result=[{
                    "product_id"      : product.product.id,
                    "product_kr_name" : product.product.kr_name,
                    "product_en_name" : product.product.en_name,
                    "product_price"   : product.product.price,
                    "product_image"   : [image.url for image in product.image_set.all()]
            }]
        return JsonResponse({'result' : result}, status=200)