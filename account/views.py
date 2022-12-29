from rest_framework import generics
from .models import *
from .serializers import AccountSerializers
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination

class AccountAPIListPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000

class AccountAPIUpdatePagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class AccountAPIList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializers
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = AccountAPIListPagination

class AccountAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializers
    permission_classes = (IsAuthenticated, )
    pagination_class = AccountAPIUpdatePagination
    # authentication_classes = (TokenAuthentication, ) 

class AccountAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializers 
    permission_classes = (IsAdminOrReadOnly, )




