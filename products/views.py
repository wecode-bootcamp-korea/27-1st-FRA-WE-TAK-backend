from django.http.response  import JsonResponse
from django.http.response  import JsonResponse

from django.views          import View

from .models               import MainCategory


class CategoryView(View):
    def get(self, request):
        maincategories        = MainCategory.objects.prefetch_related('subcategory_set')
        results = []
        for maincategory in maincategories:
            subcategories     = maincategory.subcategory_set.all()
            sub_category_list = []
            for subcategory in subcategories:
                sub_category_list.append(
                    {
                        'id'            : subcategory.id,
                        'kr_name'       : subcategory.kr_name,
                        'thumbnail_url' : subcategory.thumbnail_url,
                    }
                )
            results.append({
                'name'                  : maincategory.name,
                'sub_category_list'     : sub_category_list
            })
        return JsonResponse({"result":results}, status=200) 