from rest_framework.permissions import BasePermission
from decouple import config


class Check_API_KEY_Auth(BasePermission):
    def has_permission(self, request, view):
        # API_KEY should be in request headers to authenticate requests
        api_key_secret = request.META.get('API_KEY')
        if 'api_key' in request.headers:
            api_key_secret = request.headers['api_key']
            if api_key_secret == config('SECRET_KEY'):
                print('FOUND')
        print(request.user)
        return api_key_secret == config('SECRET_KEY')

