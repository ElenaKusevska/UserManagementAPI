from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets, filters
from rest_framework.response import Response
from myproject.utils import PasswordTooShortException

from rest_framework.pagination import PageNumberPagination

class UserViewSetPagination(PageNumberPagination):
    page_size = 2


class UserViewSet(viewsets.ModelViewSet):
    pagination_class = UserViewSetPagination
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()

        username = self.request.query_params.get('name')
        if username is not None:
            queryset = queryset.filter(username=username)

        email = self.request.query_params.get('email')
        if email is not None:
            queryset = queryset.filter(email=email)
        return queryset
    


    def validate_request_data(self, request_method, request_data):

        # For example to check that password is not too short:
        print("-----------------------")
        print(request_method)
        print("-----------------------")
        if request_method == "POST":
            if "password" in request_data.keys():
                if len(request_data["password"]) < 8:
                    raise(PasswordTooShortException)


    def get_serializer_context(self):
        context = super().get_serializer_context()
        self.validate_request_data(context["request"].method, context["request"].data,)
        return context

        



    


