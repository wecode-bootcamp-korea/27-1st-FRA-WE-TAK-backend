from django.http.response  import JsonResponse

from django.views          import View

from products.models       import Product

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
        products = Product.objects.all()
        results =[{
                'product_id'         : product.id,
                'kr_name'            : product.kr_name,
                'en_name'            : product.en_name,
                'price'              : product.price,
                'sub_category_id'    : product.sub_category.id,
                'sub_category_name'  : product.sub_category.kr_name,
                'main_category_name' : product.sub_category.main_category.name,
                'main_category_id'   : product.sub_category.main_category.id,
                'images' : [{
                    "image_id"       : image.id,
                    "product_image"  : image.url,
                    } for image in product.image_set.all()],
                'rating'        : product.rating
            }for product in products]
            
        return JsonResponse({"result":results}, status=200)
>>>>>>> main
