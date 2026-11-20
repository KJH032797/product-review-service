from django.shortcuts import render
from rest_framework.viewsets import ViewSet

# Create your views here.
class UserViewSet(ViewSet):

    def list(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass