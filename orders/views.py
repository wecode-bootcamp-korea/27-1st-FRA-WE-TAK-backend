import json

from django.http.response   import JsonResponse
from django.views           import View

from .models                import Cart
from FRA_WE_BACK.core.utils import log_in_decoratorr


class CartView(View):
    @log_in_decoratorr
    def get(self, request):
            carts  = Cart.objects.filter(user = request.user)
            cart_items = []
            for cart in carts:
                cart_items = [{
                    "product_id"      : cart.product.id,
                    "product_kr_name" : cart.product.kr_name,
                    "product_en_name" : cart.product.en_name,
                    "product_price"   : cart.product.price,
                    "count"           : cart.count,
                    "product_image"   : [image.url for image in cart.product.image_set.all()]
                }]
            return JsonResponse({'cart_items' : cart_items}, status=200)

    @log_in_decoratorr
    def post(self, request):
        try:
            data               = json.loads(request.body)
            Cart.objects.create(
                product_id     = data['product_id'],
                user           = request.user,
                count          = data['count']
            )
            return JsonResponse({'message' : 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

    @log_in_decoratorr
    def patch(self, request, cart_id):
        try:
            data = json.loads(request.body)
            cart = Cart.objects.get(id=cart_id)

            if data['cart_button'] == '증가':
                cart.count += 1
                cart.save()
            elif data['cart_button'] == '감소':
                if cart.count == 1:
                    return JsonResponse({'message':'INVALID REQUEST'}, status=401)
                cart.count -= 1
                cart.save()
            
            return JsonResponse({'message':'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400) 

    @log_in_decoratorr
    def delete(self, request, cart_id):
        try:
            data = json.loads(request.body)
            cart = Cart.objects.get(id=cart_id)
            if data['cart_delete'] == '삭제':
                cart.delete()
            
            return JsonResponse({'message':'SUCCESS'}, status=200)

        except Cart.DoesNotExist:
            return JsonResponse({'message':'NOT_FOUND'}, status=401)

