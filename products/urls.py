from django.urls import path

from products.views      import CategoryView, ProductListView, ProductView

urlpatterns = [
    path('/category', CategoryView.as_view()),
    path('', ProductListView.as_view()),
    path('/<int:product_id>', ProductView.as_view())
]
