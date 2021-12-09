import json, uuid

from django.http.response   import JsonResponse
from django.views           import View

from .models                import Cart, Order, OrderItem
from FRA_WE_BACK.core.utils import log_in_decorator


class CartView(View):
    @log_in_decorator
    def get(self, request):
            carts  = Cart.objects.filter(user=request.user).select_related("product").prefetch_related("product__image_set")
    
            results = [{
                "cart_id"         : cart.id,
                "user_id"         : request.user.id,
                "email"           : request.user.email,
                "name"            : request.user.name,
                "product_id"      : cart.product.id,
                "product_kr_name" : cart.product.kr_name,
                "product_en_name" : cart.product.en_name,
                "product_price"   : cart.product.price,
                "count"           : cart.count,
                "product_image"   : [image.url for image in cart.product.image_set.all()]
            }for cart in carts]
            return JsonResponse({'cart_items' : results}, status=200)


    @log_in_decorator
    def post(self, request):
        try:
            data               = json.loads(request.body)

            Cart.objects.create(
                user           = request.user,
                product_id     = data['product_id'],
                count          = data['count']
            )
            return JsonResponse({'message' : 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

    @log_in_decorator
    def patch(self, request, cart_id):
        try:
            data = json.loads(request.body)
            cart = Cart.objects.get(id=cart_id, user_id= request.user.id)
            cart.count = data["count"]
            cart.save()
           
            return JsonResponse({'message':'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400) 


    @log_in_decorator
    def delete(self, request, cart_id):
        Cart.objects.filter(id=cart_id, user_id = request.user.id).delete()
        return JsonResponse({'message':'NO CONTENT'}, status=204)


class OrderStatus(Enum):    
    WAIT_DEPOSIT       = 1   
    COMPLETION_DEPOSIT = 2    
    READY_RELEASE      = 3  
    SHIPMENT_COMPLETE  = 4
    DELIVERED          = 5
    DELAYED_DELIVERY   = 6
    DELIVERY_COMPLETED = 7
    ORDER_COMPLETE     = 8
    ORDER_CANCELLATION = 9    
class OrderView(View):
    @log_in_decorator
    def post(self, request):
        try:
            data       = json.loads(request.body)
            user       = request.user
            order = Order.objects.create(
                {
                    "order_number"    : uuid.uuid4(),
                    "order_status_id" : 1,
                    "user_id"         : user.id   
                }
            )
            bulk_list = [OrderItem(
                {   
                    "order_item_status"  : 1,            
                    "count"              : data["count"],
                    "tracking_number"    : uuid.uuid4(),
                    "address"            : data["address"],
                    "product"            : [{"product_id" :OrderItem.product.id} for i in OrderItem.product],
                    "order"              : order.id,
                }for carts in Cart)]
            
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)
    # def get(self, request):


