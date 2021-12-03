import re, json, bcrypt, jwt

from django.http     import JsonResponse
from django.views    import View

from .models         import User
from FRA_WE_BACK.settings import SECRET_KEY

class SignUpView(View):
    def post(self, request):
        try:
            data          = json.loads(request.body)
            user_name     = data['name']
            user_email    = data['email']
            user_password = data['password']
            user_contact  = data['contact']
            user_address  = data['address']

            if User.objects.filter(email=user_email).exists():
                return JsonResponse({"message":"EMAIL_ALREADY_EXIST"}, status=400)

            if not re.match('^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$', user_email):
                return JsonResponse({"message" : "EMAIL_ERROR"}, status=400)

            if not re.match('^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}$',user_password):
                return JsonResponse({"message" : "PASSWORD_ERROR"}, status=400)

            hashed_password = bcrypt.hashpw(user_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create( 
                name         = user_name,
                email        = user_email,
                password     = hashed_password,
                contact      = user_contact,
                address      = user_address,
            )
            return JsonResponse({"message":"SUCCESS"}, status=201) 

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)