from django.urls     import path
from products.views  import ListPageView#DetailPageView

urlpatterns = [
    path('/main/<int:sub_category_id>',ListPageView.as_view()),
    #path('/main/<int:sub_category_id>/<int:prodcut_id',DetailPageView.as_view())
]