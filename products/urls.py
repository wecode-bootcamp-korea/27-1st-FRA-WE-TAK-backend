from django.urls import path
from products.views      import ListPageView

urlpatterns = [
    path('/main/<int:sub_category_id>',ListPageView.as_view())
]