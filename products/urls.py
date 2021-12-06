from django.urls import path

from .views      import CategoryView, SearchView

urlpatterns = [
    path('/category', CategoryView.as_view()),
    path('/search', SearchView.as_view())

]
