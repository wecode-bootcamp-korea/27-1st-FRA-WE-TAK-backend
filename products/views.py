from django.http.response  import JsonResponse
from django.views          import View
from products.models       import Product

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
                'description_img'   : product.description
            }
        except Product.DoesNotExist:
            return ..

        return JsonResponse({"result":result}, status=200) 
