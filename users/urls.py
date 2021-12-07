from django.urls import path
from .views      import SignUpView, LoginView, EmailSearchView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/login', LoginView.as_view()),
    path('/emailsearch', EmailSearchView.as_view() )
]
