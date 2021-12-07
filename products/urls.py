from django.urls import path

from .views      import CartegoryView, ProductListView

urlpatterns = [
    path('/category', CartegoryView.as_view()),
    path('',ProductListView.as_view())
]
