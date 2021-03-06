import jwt

from django.http 	        import JsonResponse    

from FRA_WE_BACK.settings     import SECRET_KEY, ALGORITHM                             
from users.models             import User


def log_in_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token   = request.headers.get('Authorization', None)          
            payload        = jwt.decode(access_token, SECRET_KEY, algorithms=ALGORITHM)  
            user           = User.objects.get(id=payload['id'])


        except jwt.exceptions.DecodeError:                                        
            return JsonResponse({'message' : 'INVALID_TOKEN'}, status=400)

        except User.DoesNotExist:                                         
            return JsonResponse({'message' : 'INVALID_USER'}, status=400)

        return func(self, request, *args, **kwargs)

    return wrapper