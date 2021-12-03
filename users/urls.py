from django.urls import path
from .views      import SignUpView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/login', SignUpView.as_view())
]

