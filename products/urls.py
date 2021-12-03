from django.urls import path
from .views      import ListPageView

urlpatterns = [
    path('/list_page', ListPageView.as_view())
]