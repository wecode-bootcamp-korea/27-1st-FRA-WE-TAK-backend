from django.urls import path

from .views      import SubCategoryView

urlpatterns = [
    path('/sub-category', SubCategoryView.as_view())
]
