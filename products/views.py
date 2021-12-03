from django.http.response  import JsonResponse
from django.views          import View
from django.http.response  import JsonResponse

from .models               import MainCategory

class SubCategoryView(View):
    def get(self, request):
        item = MainCategory.objects.prefetch_related('subcategory_set')
        results = []
        for items in item:
            subcategory = items.subcategory_set.all()
            sub_category_list = []
            for subcategories in subcategory:
                sub_category_list.append(
                    {
                        'id'            : subcategories.id,
                        'kr_name'       : subcategories.kr_name,
                        'thumbnail_url' : subcategories.thumbnail_url,
                    }
                )
            results.append({
                'name' : items.name,
                'sub_category_list' : sub_category_list
            })
        return JsonResponse({"result":results}, status=200) 