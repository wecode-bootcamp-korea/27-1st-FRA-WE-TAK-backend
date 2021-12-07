from django.urls import path
<<<<<<< HEAD

urlpatterns = [
   # path('/signup', SignUpView.as_view()),
   # path('/login', LoginView.as_view())
]

=======
from .views      import SignUpView, LoginView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/login', LoginView.as_view())
]
>>>>>>> main
