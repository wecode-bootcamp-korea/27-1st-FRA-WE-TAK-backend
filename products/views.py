from django.http.response  import JsonResponse
from django.http.response  import JsonResponse

from django.views          import View

from .models               import MainCategory


class SubCategoryView(View):
    def get(self, request):
        items   = MainCategory.objects.prefetch_related('subcategory_set')
        results = []
        for item in items:
            subcategory       = item.subcategory_set.all()
            sub_category_list = []
            for subcategory in subcategory:
                sub_category_list.append(
                    {
                        'id'            : subcategory.id,
                        'kr_name'       : subcategory.kr_name,
                        'thumbnail_url' : subcategory.thumbnail_url,
                    }
                )
            results.append({
                'name' : item.name,
                'sub_category_list' : sub_category_list
            })
        return JsonResponse({"result":results}, status=200) 