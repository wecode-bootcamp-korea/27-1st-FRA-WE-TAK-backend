from django.urls import path
from .views      import SignUpView, LoginView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
<<<<<<< Updated upstream
    path('/login', LoginView.as_view())
]
=======
    path('/login', LoginView.as_view()),
    path('/search-email', search_email)
]
>>>>>>> Stashed changes
