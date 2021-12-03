from django.http.response  import JsonResponse
from django.views          import View
from django.http.response  import JsonResponse

from .models               import SubCategory, MainCategory

class SubCategoryView(View):
    def get(self, request, maincategory_id):
        items = SubCategory.objects.filter(main_category__id = maincategory_id).all()
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