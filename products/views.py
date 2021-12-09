from django.http.response import JsonResponse
from django.views         import View
from django.http.response import JsonResponse
from django.db.models     import Q

from products.models      import Product, MainCategory


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

class ProductListView(View):
    def get(self, request):
        offset         = int(request.GET.get("offset", None))
        limit          = int(request.GET.get("limit", None))
        search_keyword = request.GET.get("search")
        q = Q()
        if search_keyword:
            q &= Q(kr_name__contains=search_keyword) | Q(en_name__contains=search_keyword)
        products = Product.objects.filter(q)[offset:limit]
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

class ProductView(View):
    # 8000:products/1
    def get(self, request, product_id):
        try:
            product = Product.objects.select_related("sub_category").get(id = product_id)

            result = {
                'product_id'        : product.id,
                'kr_name'           : product.kr_name,
                'en_name'           : product.en_name,
                'price'             : product.price,
                'sub_category_id'   : product.sub_category.id,
                'sub_category_name' : product.sub_category.kr_name,
                'rating'            : product.rating,
                'description_img'   : product.description,
                'images'            : [{"id" : image.id, "url" : image.url} for image in product.image_set.all()]

            }
        except Product.DoesNotExist:
            return JsonResponse({"message": 'Product_Not_Exists'}, status=404)

        return JsonResponse({"result":result}, status=200)