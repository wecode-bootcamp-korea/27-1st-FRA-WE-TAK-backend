from django.http.response  import JsonResponse
from django.views          import View
from django.http.response  import JsonResponse
from .models               import Product 


class ListPageView(View):
    def get(self, request, subcategory_id):
        items = Product.objects.filter(sub_category__id = subcategory_id).all()
        results = []
        for i in items:
                results.append(
                    {
                        'id'            : i.id,
                        'kr_name'       : i.kr_name,
                        'thumbnail_url' : i.thumbnail_url,
                    }
                )
        return JsonResponse({"result":results}, status=200) 