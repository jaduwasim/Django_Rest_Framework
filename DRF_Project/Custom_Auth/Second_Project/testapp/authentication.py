'''
1. Client Required Secrate Key and username as query parameter
2. Length of key should be 7 character
3. The first character of key should be lower case alphabate symbol which shuld be last character of username 
4. The third character should be Z.
5. The fifth character should be first charcter of username

username = durga
secrete Key = abZcdef

username = jadu
secrate key = uaZbjbc
'''

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.GET.get('username')
        key = request.GET.get('key')
        if username is None:
            raise AuthenticationFailed('please provide username!! your username is missing')
        elif key is None:
            raise AuthenticationFailed('please provide key, your key is missing')
        case_1 = len(key) == 7
        case_2 = key[0] == username[-1].lower()
        case_3 = key[2] == 'Z'
        case_4 = key[4] == username[0]

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed('Your Provided username is invalid, please provide valid username')
        if case_1 and case_2 and case_3 and case_4:
            return (user, None)
        raise AuthenticationFailed('Your Provided Key is Invalid, please provide valid Key')
        



        