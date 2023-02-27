import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from analyze.models import *
from rest_framework import serializers
from analyze.models import Analyze, Category


class AnalyzeSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Analyze
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    children = AnalyzeSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'date', 'children', ]

    # def get_fields(self):
    #     fields = super().get_fields()
    #     fields['children'] = CategorySerializer(many=True, read_only=True)
    #     return fields
