from django.urls import path
from .views      import SignUpView, LoginView, UserResetView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/login', LoginView.as_view()),
    path('/usersearch', UserResetView.as_view() )
]
