from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import CategorySerializer
from .models import Category

# FBV - function base view (decorators)
# CBV - class base view (APIViews, generics, ModelViewSet)
# GET PUT POST DELETE

class CategoryView(APIView):

    def post(self, request):
        post = request.POST
        # print(post)
        serializer = CategorySerializer(data=post) # data - argument (POST, PUT, PATCH)
        if serializer.is_valid(raise_exception=True):
            # print(serializer.validated_data)
            Category.objects.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def get(self, request):   # views
    #     category = Category.objects.all() # Queryset[] [1,2,3,4] (ORM request) PythonObject -> JSON
    #     serializer = CategorySerializer(category, many=True) # PythonObject -> JSON
    #     data = serializer.data
    #     return Response(data, status=status.HTTP_200_OK)

                   # OR

class CategoryListView(ListAPIView):   # generics

    queryset = Category.objects.all()
    serializer_class = CategorySerializer



