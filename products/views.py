import json

from django.http.response  import JsonResponse
from django.views          import View

from django.db.models import Q

from .models               import MainCategory, Product

class CartegoryView(View):
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

class ProductListView(View):
    def get(self, request):
        offset         = request.GET.get("offset", 0)
        limit          = request.GET.get("limit", 100)
        search_keyword = request.GET.get("search")
        print(search_keyword)

        q = Q()

        if search_keyword:
            q &= Q(kr_name__contains=search_keyword) | Q(en_name__contains=search_keyword)

        products = Product.objects.filter(q)[offset: offset+limit]

        results =[{
                'product_id'         : product.id,
                'kr_name'            : product.kr_name,
                'en_name'            : product.en_name,
                'price'              : product.price,
                'sub_category_id'    : product.sub_category.id,
                'sub_category_name'  : product.sub_category.kr_name,
                'main_category_name' : product.sub_category.main_category.name,
                'main_category_id'   : product.sub_category.main_category.id,
                'images'             : [{"id" : image.id, "url" : image.url} for image in product.image_set.all()]
            }for product in products]
            
        return JsonResponse({"result":results}, status=200)
