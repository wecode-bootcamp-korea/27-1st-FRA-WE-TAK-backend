from django.http.response  import JsonResponse
from django.views          import View
from django.http.response  import JsonResponse
from products.models       import Product 


class ListPageView(View):
    def get(self, request, sub_category_id):
        products = Product.objects.filter(sub_category_id = sub_category_id)
        results =[]
        for product in products:
            results.append(
                {
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
                    }
            )
        return JsonResponse({"result":results}, status=200)