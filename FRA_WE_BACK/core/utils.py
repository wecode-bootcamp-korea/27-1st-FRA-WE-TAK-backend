import jwt

from django.http 	        import JsonResponse    

from FRA_WE_BACK.settings     import SECRET_KEY                             
from users.models             import User


def LogInDecorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization', None)          
            payload      = jwt.decode(access_token, SECRET_KEY, algorithms='HS256')  
            user   	     = User.objects.get(id=payload['id'])                 
            request.user = user

        except jwt.exceptions.DecodeError:                                        
            return JsonResponse({'message' : 'INVALID_TOKEN', 'Token':access_token }, status=400)

        except User.DoesNotExist:                                         
            return JsonResponse({'message' : 'INVALID_USER'}, status=400)

        return func(self, request, *args, **kwargs)

    return wrapper