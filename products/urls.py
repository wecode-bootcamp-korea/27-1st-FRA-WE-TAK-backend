from django.urls import path

from .views      import RandomCategoryView

urlpatterns = [
    path("products/category", RandomCategoryView.as_view())
]
