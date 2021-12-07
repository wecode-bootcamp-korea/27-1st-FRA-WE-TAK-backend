from django.urls    import path
from products.views import ProductListView

urlpatterns = [
    path('/subcategory',ProductListView.as_view())
]
