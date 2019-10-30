from .models import Post, Album, File
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    
    author_name=serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Post # Post를 기반으로 직렬화 시킬 것.
        fields = ['pk','title','body', 'author_name'] 
        # fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    
    author_name=serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Album
        fields = ['pk','author_name','image', 'desc']

class FileSerializer(serializers.ModelSerializer):
    
    author_name=serializers.ReadOnlyField(source='author.username')
    files = serializers.FileField(use_url=True)

    class Meta:
        model = File
        fields = ['pk','author_name','files', 'desc']
