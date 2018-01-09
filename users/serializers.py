from rest_framework import serializers

from users.models import Blogger


class BloggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogger
        fields = ('id', 'first_name', 'last_name', 'created', 'role')