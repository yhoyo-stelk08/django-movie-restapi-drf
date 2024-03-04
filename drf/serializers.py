from rest_framework import serializers
from .models import Movie

class MovieSerializers(serializers.ModelSerializer) :
    img = serializers.ImageField(max_length=None,use_url=True)
    class Meta :
        model = Movie
        fields = ['id','title','desc','rating','duration','year','category','img']