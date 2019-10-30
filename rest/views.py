from django.shortcuts import render
from .models import Post, Album, File
from .serializers import PostSerializer, AlbumSerializer, FileSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser

import requests
import json

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [SearchFilter]
    search_fields = ('title', 'body')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # 현재 request를 보낸 유저
    # == self.request.user

    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()

        return qs

class ImgViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

from rest_framework.response import Response
from rest_framework import status

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    # 여러가지 파일들의 타입들을 수락
    parser_class = (MultiPartParser, FormParser)
    
    # create() 오버라이딩 -> post()
    # API HTTP -> get() post()

    def post(self, request, *args, **kwargs):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=HTTP_400_BAD_REQUEST)

'''
# kakao api
print("search\n")
url = "https://dapi.kakao.com/v2/search/web"
queryString={"query":"덕성여자대학교"}
header={"Authorization":"KakaoAK 1209af700a4034334fcfa7e0e62f6e28"}
r=requests.get(url, headers=header, params=queryString)
print(json.loads(r.text))

print("local\n")
url = "https://dapi.kakao.com/v2/local/search/address.json"
queryString={"query":"백석동"}
header={"Authorization":"KakaoAK 1209af700a4034334fcfa7e0e62f6e28"}
r=requests.get(url, headers=header, params=queryString)
print(json.loads(r.text))
'''