from rest_framework import serializers

from apps.product.models import Category


# class CategorySerializer(serializers.Serializer):

#     title = serializers.CharField(max_length=150, min_length=5)
#     slug = serializers.SlugField(max_length=150)

                 # OR

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('title', 'slug')


