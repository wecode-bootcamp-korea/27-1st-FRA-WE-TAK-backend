import re, json, bcrypt, jwt, uuid, string, random

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
            data        = json.loads(request.body)
            user        = User.objects.get(name=data['name'],contact=data['contact'],email=data['email'])
        
            random_digit = uuid.uuid1().int>>64
            four_digit = ''
            for i in range(4):
                four_digit += random.choice(str(random_digit))

            four_digit.save()

            return JsonResponse({'message': four_digit}, status=200) #,'token' : jwt.encode({'id': users.id},SECRET_KEY, algorithm=ALGORITHM))

            """
            1. 사용자 인증에 필요한 4자리 인증 코드생성 예)4892 (uuid 라이브러리를 사용하면 난수를 생성 가능)
            2. user table에 인증 컬럼에 4892 저장
            3. 생성한 4892 번호 프론트에 반환
            """

        except KeyError:
            return JsonResponse({"message" : "key_error"}, status=400)

        except User.DoesNotExist:
            return JsonResponse({'message': 'user does not exist'}, status=400)
                        
    def patch(self, request):
        users = User.objects.filgter(user=request.user)
        try:
            """
            1. 이전에 반환 했던 4892 번호를 프론트에서 전달 받는다.
            2. 전달 받은 4892로 user 조회
            3. 4892 번호를 가진 user가 db에 존재하면 access_token 발급
            4. 4892 번호를 가진 user가 db에 없으면 인증 code errror 반환
            """

            data           = json.loads(request.body)
            user = request.four_digit 
            password       = data['password']
            email          = data['email']

            if not User.objects.filter(password=password).exists():
                return JsonResponse({'message': ''}, status=200)
            password       = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            user.password  = password
            user.save()
            return JsonResponse({'message': ''}, status=200) #,'token' : jwt.encode({'id': users.id},SECRET_KEY, algorithm=ALGORITHM))
            
        except KeyError:
            return JsonResponse({"message" : "key_error"}, status=400)

        except User.DoesNotExist:
            return JsonResponse({'message': 'user does not exist'}, status=400)