from django.http.response  import JsonResponse
from django.views          import View

from products.models       import MainCategory, Product

class CategoryView(View):
    def get(self, request):
        main_categories = MainCategory.objects.prefetch_related('subcategory_set')
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
        offset = request.Get.get('offset', None)
        limit = request.Get.get('limit', None)
        products = Product.objects.all()[offset:offset+ limit]
        results = [{
                        'product_id'         : product.id,
                        'kr_name'            : product.kr_name,
                        'en_name'            : product.en_name,
                        'price'              : product.price,
                        'sub_category_id'    : product.sub_category.id,
                        'sub_category_name'  : product.sub_category.kr_name,
                        'main_category_name' : product.sub_category.main_category.name,
                        'main_category_id'   : product.sub_category.main_category.id,
                        'rating'             : product.rating,
                        'images' : [{
                            "id"       : image.id,
                            "url"  : image.url,
                            } for image in product.image_set.all()],                  
                        }for product in products]

        return JsonResponse({"result":results}, status=200)

class ProductView(View):
    def get(self, request, product_id):
        products = Product.objects.select_related("sub_category").get(id = product_id)
        results =[{
            'product_id'           : product.id,
            'kr_name'              : product.kr_name,
            'en_name'              : product.en_name,
            'price'                : product.price,
            'sub_category_id'      : product.sub_category.id,
            'sub_category_kr_name' : product.sub_category.kr_name,
            'sub_category_en_name' : product.sub_category.en_name,
            'rating'               : product.rating,
            'description_txt'      : product.title,
            'description_img'      : product.description
        } for product in products]
        return JsonResponse({"result":results}, status=200)
        