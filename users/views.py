import re, json, bcrypt, jwt

from django.http     import JsonResponse
from django.views    import View

from .models         import User
from FRA_WE_BACK.settings import SECRET_KEY

class LoginView(View):
    def post(self, request):
        try:
            data           = json.loads(request.body)
            user_email     = data['email']
            user_password  = data['password']
            user           = User.objects.get(email=user_email)

            if bcrypt.checkpw(user_password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({"message": "invalid_password"}, status=401)

            token = jwt.encode ({'id':user.id}, SECRET_KEY, algorithm='HS256')

            return JsonResponse({
                'message' : 'success', 
                "token" : token
                }, status=200)

        except KeyError:
            return JsonResponse({"message" : "key_error"}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'message' : 'invalid_email'}, status=401)
