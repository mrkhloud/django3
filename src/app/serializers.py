from rest_framework import serializers

from . import models


class MySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Article
        fields = '__all__'


# class MySerializer2(serializers.Serializer):
#     title = serializers.CharField()
#     content = serializers.CharField()
#     date_add = serializers.DateTimeField(read_only=True)
#     status = serializers.BooleanField(default=True)
#     category_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return models.Article.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.date_add = validated_data.get('date_add', instance.date_add)
#         instance.status = validated_data.get('status', instance.status)
#         instance.category_id = validated_data.get('category_id', instance.category_id)
#         instance.save()
#         return instance
