from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NameSeializer
# Create your views here.

class TestAPIView(APIView):
    def get(self, request, *args, **kwagrs):
        color = ['RED','GREEN','WHITE','BLACK','PINK']
        return Response({'msg':'Hello Happy Pongal', 'color':color})
    
    def post(self, request, *args, **kwargs):
        # print(request.body) / Output b'{"name":"Entered name"}' it will come in json form as it is
        # print(request.data) / Output {'name': 'washim'}, it will come in python native data type
        serialize = NameSeializer(data=request.data)
        if serialize.is_valid():
            name = serialize.data.get('name')
            msg = f'Hello {name}, Happy New Year!'
            return Response({'msg':msg})
        return Response(serialize.errors)

    def put(self, request,pk = None, *args, **kwargs):
        return Response({'msg':'This Response from Put Request'})
    
    def patch(self, request, pk=None, *args, **kwargs):
        return Response({'msg':'This response from patch methods'})

    def delete(self, request,pk=None, *args, **kwargs):
        return Response({'msg':'This Response from Delete request'})
    
from rest_framework.viewsets import ViewSet
class TestViewSET(ViewSet):

    def list(self, request , *args, **kwargs):
        color = ['RED','GREEN','WHITE','BLACK','PINK']
        return Response({'msg':'Hello Happy Pongal', 'color':color})
    
    def retrives(self, request,pk=None, *args, **kwargs):
        return Response({'msg':'This Response from retrive method'})

    def create(self, request, *args, **kwargs):
        serialize = NameSeializer(data=request.data)
        if serialize.is_valid():
            name = serialize.data.get('name')
            msg = f'Hello {name}, Happy Eid !'
            return Response({'msg':msg})
        return Response(serialize.errors)
    
    def update(self, request,pk=None, *args, **kwargs):
        return Response({'msg':'This respose from Update Methods'})

    def partial_update(self, request, pk=None, *args, **kwargs):
        return Response({'msg':'This Response form Partial Update'})

    def destroy(self, request, pk=None, *args, **kwargs):
        return Response({'msg':'This response from destroy method'})