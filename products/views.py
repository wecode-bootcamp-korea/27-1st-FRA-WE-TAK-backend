from django.http.response  import JsonResponse

from django.views          import View

from .models               import MainCategory


class CategoryView(View):
    def get(self, request):
        main_categories       = MainCategory.objects.prefetch_related('subcategory_set')

        results = []

        for main_category in main_categories:
            subcategories     = main_category.subcategory_set.all()
            results.append({
                'name'                  : main_category.name,
                'sub_category_list'     : [{
                    'id' : sub_category_list.id, 
                    'kr_name' : sub_category_list.kr_name, 
                    'thumbnail_url' : sub_category_list.thumbnail_url
                    } for sub_category_list in subcategories]
            })
        return JsonResponse({"result":results}, status=200) 