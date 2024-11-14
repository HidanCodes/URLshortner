import random

from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from tutorial.quickstart.serializers import UserSerializer
from django.contrib.auth.models import User

from .models import Urls
from .serializer import UrlSerializer, MyUserSerializer


def index(request):
    return render(request, 'homepage.html')


class MakeUrls(APIView):
    def get(self, request):

        rand_num = random.randint(100000, 1000000)
        while Urls.objects.filter(number=rand_num).exists():
            rand_num = random.randint(100000, 999999)
        data = {'url': request.query_params.get('url'), 'number': rand_num}
        serializer = UrlSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("bad url", status=status.HTTP_400_BAD_REQUEST)


class AllUrls(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        url = Urls.objects.all()
        serial = UrlSerializer(url, many=True)
        return Response(serial.data)


class UrlDetail(APIView):
    def get(self, request, pk):
        try:
            p = Urls.objects.get(number=pk)

        except Urls.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        return Response(UrlSerializer(p).data)


class RedirectUrl(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, id):
        if Urls.objects.filter(number=id).exists():
            url = Urls.objects.get(number=id)
            return redirect(url.url)
        else:
            return HttpResponse("hamchin linki nadarim", status=status.HTTP_404_NOT_FOUND)

class RegisterUser(APIView):
    def post(self, request):
        serializer = MyUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("kharab shod", status=status.HTTP_400_BAD_REQUEST)

class AllUsers (APIView):
    def get (self , request):
        serializer = MyUserSerializer(User.objects.all(), many=True)
        return Response(serializer.data)
