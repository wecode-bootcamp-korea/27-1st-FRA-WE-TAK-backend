from django.urls import path
from .views      import SignUpView, LoginView, UserResetView, PasswordresetView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/login', LoginView.as_view()),
    path('/usersearch', UserResetView.as_view()),
    path('/passwordreset', PasswordresetView.as_view())
]
