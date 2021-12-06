import json

from django.http.response import JsonResponse
from django.views         import View

from .models              import Product

class SearchView(View):
    def get(self, request):
        data    = json.loads(request.body)
        products = Product.objects.filter(kr_name=data['search'])
        results = []

        for product in products:
            results=[{
                    "product_id"      : product.id,
                    "product_kr_name" : product.kr_name,
                    "product_en_name" : product.en_name,
                    "product_price"   : product.price,
                    "product_image"   : [image.url for image in product.image_set.all()]
            }]
        return JsonResponse({'result' : results}, status=200)