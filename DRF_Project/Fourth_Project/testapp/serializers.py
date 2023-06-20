from rest_framework import serializers

class NameSeializer(serializers.Serializer):
    name = serializers.CharField(max_length = 7)