import jwt
from django.conf import settings
from django.http import JsonResponse
from user.models import User, UserSelectedAccount

class JWTAccountMiddleware:
    WHITELIST_API_PATHS = [
        '/api/token/',
        '/api/token/refresh/',
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_path = request.path

        if (not request_path.startswith('/api')) or (request_path in self.WHITELIST_API_PATHS):
            return self.get_response(request)

        token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload['user_id']
            user_selected_account = UserSelectedAccount.objects.get(user_id=user_id)
            request.selected_account = user_selected_account.selected_account
            response = self.get_response(request)
        except jwt.DecodeError:
            response = JsonResponse({'message': 'Invalid token'}, status=400)
        except jwt.ExpiredSignatureError:
            response = JsonResponse({'message': 'Token expired'}, status=401)
        except User.DoesNotExist:
            response = JsonResponse({'message': 'User not found'}, status=400)
        except UserSelectedAccount.DoesNotExist:
            response = JsonResponse({'message': 'User account not found'}, status=400)

        return response
