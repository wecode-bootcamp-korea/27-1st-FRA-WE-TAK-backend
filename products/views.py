import json

from django.http.response  import JsonResponse
from django.views          import View

from .models               import MainCategory, Product


class CategoryView(View):
    def get(self, request):
        main_categories       = MainCategory.objects.prefetch_related('subcategory_set')
        results = []

        for main_category in main_categories:
            sub_categories     = main_category.subcategory_set.all()
            results.append({
                'name'                  : main_category.name,
                'sub_category_list'     : [{
                    'id'                : sub_category.id, 
                    'kr_name'           : sub_category.kr_name, 
                    'thumbnail_url'     : sub_category.thumbnail_url
                    } for sub_category in sub_categories]
            })
        return JsonResponse({"result":results}, status=200) 


class SearchView(View):
    def get(self, request):
        try:
            data    = json.loads(request.body)
            products = Product.objects.filter(kr_name__icontains=data['search'])
            results = []

            for product in products:
                results.append([{
                        "product_id"      : product.id,
                        "product_kr_name" : product.kr_name,
                        "product_en_name" : product.en_name,
                        "product_price"   : product.price,
                        "product_image"   : [image.url for image in product.image_set.all()]
                }])
            return JsonResponse({'result' : results}, status=200)
        except KeyError:
            JsonResponse({'message':'KEY_ERROR'}, status=400)



