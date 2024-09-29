from rest_framework.exceptions import APIException

class PasswordTooShortException(APIException):
    status_code = 422
    default_detail = 'Password is too short, must contain at least 8 characters'
    default_code = 'Invalid Password'