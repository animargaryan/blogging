import django_filters
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Blogger
from users.serializers import BloggerSerializer


class BloggerFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    year_joined = django_filters.NumberFilter(name='created', lookup_expr='year')

    class Meta:
        model = Blogger
        fields = ['first_name', 'last_name']


class BloggersSearchList(generics.ListAPIView):
    """
      List bloggers by first name and last name with contains filter and with year of created field
    """
    queryset = Blogger.objects.all()
    serializer_class = BloggerSerializer
    filter_class = BloggerFilter


class BloggersList(APIView):
    """
       List all bloggers, or create a new blogger.
    """

    def get(self, request, format=None):
        bloggers_list = Blogger.objects.all()
        serializer = BloggerSerializer(bloggers_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BloggerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
