from django.urls    import path
from products.views import CategoryView, ProductListView

urlpatterns = [
    path('/category', CategoryView.as_view()),
    path('/subcategory',ProductListView.as_view())
]
