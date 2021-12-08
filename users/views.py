import re, json, bcrypt, jwt

from django.http            import JsonResponse
from django.core.exceptions import ValidationError
from django.views           import View


from .models              import User
from users.validation     import email_check, password_check
from FRA_WE_BACK.settings import SECRET_KEY, ALGORITHM

class SignUpView(View):
    def post(self, request):
        try:
            data          = json.loads(request.body)
            user_name     = data['name']
            user_email    = data['email']
            user_password = data['password']
            user_contact  = data['contact']
            user_address  = data['address']

            email_check(user_email)
            password_check(user_password)

            if User.objects.filter(email=user_email).exists():
                return JsonResponse({"message":"EMAIL_ALREADY_EXIST"}, status=400)

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

        except ValidationError as e: 
            return JsonResponse({"message": e.message}, status=400)

class LoginView(View):
    def post(self, request):
        try:
            data           = json.loads(request.body)
            user_email     = data['email']
            user_password  = data['password']
            user           = User.objects.get(email=user_email)

            if not bcrypt.checkpw(user_password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({"message": "invalid_password"}, status=401)
            
            token = jwt.encode({"id": user.id}, SECRET_KEY, algorithm=ALGORITHM)
    
            return JsonResponse({
                'message' : 'success', 
                "token"   : token
                }, status=200)

        except KeyError:
            return JsonResponse({"message" : "key_error"}, status=400)
            
        except User.DoesNotExist:
            return JsonResponse({'message' : 'invalid_email'}, status=401)

class UserResetView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            users    = User.objects.filter(name=data['name'],contact=data['contact'])

            if not users.exists():
                return JsonResponse({"message": "user does not exists"}, status=404)

            results = [user.email for user in users]

            return JsonResponse({"result":results}, status=200)

        except KeyError:
            return JsonResponse({"message" : "key_error"}, status=400)

class PasswordresetView(View):
    def post(self, request):
        # 휴대폰 인증 api
        try:
            data       = json.loads(request.body)
            password   = data['password']
            email      = data['email']
            
            if password:
                user           = User.objects.get(email=email)
                password       = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                user.password  = password
                user.save()
            else:
                user    = User.objects.get(name=data['name'],contact=data['contact'],email=data['email'])
                
                if user:
                    return JsonResponse({'message': 'user exitst'}, status=200) #,'token' : jwt.encode({'id': users.id},SECRET_KEY, algorithm=ALGORITHM))
            
        except KeyError:
            return JsonResponse({"message" : "key_error"}, status=400)

        except User.DoesNotExist:
            return JsonResponse({'message': 'user does not exist'}, status=400)
            
    # def patch(self, request):
    #     # 인증 후 비밀번호 변경 api
    #     try:
    #         data           = json.loads(request.body)

    #         user           = User.objects.get(email=email)
    #         password       = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    #         return JsonResponse({'message': ''}, status=200) #,'token' : jwt.encode({'id': users.id},SECRET_KEY, algorithm=ALGORITHM))
            
    #     except KeyError:
    #         return JsonResponse({"message" : "key_error"}, status=400)

    #     except User.DoesNotExist:
    #         return JsonResponse({'message': 'user does not exist'}, status=400)