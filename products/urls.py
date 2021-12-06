from django.urls     import path, include
from products.views  import ProductDetailView, SubCategoryView

urlpatterns = [
    path('/<int:sub_category_id>', SubCategoryView.as_view()),
    path('/subcategory/<int:product_id>', ProductDetailView.as_view())
]