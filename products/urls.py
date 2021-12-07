from django.urls import path

from .views      import CategoryView, SearchView, ProductListView

urlpatterns = [
    path('/category', CategoryView.as_view()),
    path('/search', SearchView.as_view()),
    path('',ProductListView.as_view())
]
