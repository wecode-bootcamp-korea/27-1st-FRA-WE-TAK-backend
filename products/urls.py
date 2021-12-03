from django.urls import path

from .views      import SubCategoryView

urlpatterns = [
    path('/subcategory/<int:maincategory_id>', SubCategoryView.as_view())
]
