from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from myproject.utils import PasswordTooShortException

from rest_framework.pagination import PageNumberPagination

class UserViewSetPagination(PageNumberPagination):
    page_size = 2


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserViewSetPagination


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

        



    


