from django.urls import path

from products.views      import CategoryView, SubCategoryView, ProductDetailView

urlpatterns = [
    path('/category', CategoryView.as_view()),
    path('/subcategory', SubCategoryView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view())
]