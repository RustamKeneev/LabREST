import mixins as mixins
from django.forms import model_to_dict
from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet

from .models import *
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import AnalyzeSerializer, CategorySerializer


class AnalyzeHome(ListView):
    model = Analyze
    template_name = 'analyze/analyze.html'

# class AnalyzeAPIView(generics.ListAPIView):
#     queryset = Analyze.objects.all()
#     serializer_class = AnalyzeSerializer

# class AnalyzeAPIView(APIView):
#     def get(self, request):
#         lists = Analyze.objects.all().values()
#         return Response({'analyzes': list(lists)})
#
#     def post(self, request):
#         post_new = Analyze.objects.create(
#             title=request.data['title'],
#             description=request.data['description'],
#             preparationForAnalysis=request.data['preparationForAnalysis'],
#             requirements=request.data['requirements'],
#             interpretationOfResults=request.data['interpretationOfResults'],
#             category_id=request.data['category_id'],
#             laboratoryTest=request.data['laboratoryTest'],
#             biomaterial=request.data['biomaterial'],
#             deadlineDateOfIssueOfResults=request.data['deadlineDateOfIssueOfResults']
#         )
#         return Response({'post': model_to_dict(post_new)})


class AnalyzeAPIUpdate(generics.UpdateAPIView):
    queryset = Analyze.objects.all()
    serializer_class = AnalyzeSerializer


class AnalyzeAPIIDetalView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Analyze.objects.all()
    serializer_class = AnalyzeSerializer


class AnalyzeAPIView(APIView):
    def get(self, request):
        analyze = Analyze.objects.all()
        return Response({'analyzes': AnalyzeSerializer(analyze, many=True).data})

    def post(self, request):
        serializer = AnalyzeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error":"Method put not allowed"})
        try:
            instance = Analyze.objects.get(pk=pk)
        except:
            return Response({"error":"Objects does not exists"})
        serializer = AnalyzeSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post":serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk",None)
        if not pk:
            return Response({"error":"Method DELETE not allowed"})
        return Response({"post":"delete post " + str(pk)})


class AnalyzeAPILists(generics.ListCreateAPIView):
    queryset = Analyze.objects.all()
    serializer_class = AnalyzeSerializer


class CategoryListAPI(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class AnalyzeViewSet(viewsets.ModelViewSet):
    queryset = Analyze.objects.all()
    serializer_class = AnalyzeSerializer


    # @action(method=['get'], detail=False)
    # def category(self, request):
    #     categories = Category.objects.all()
    #     return Response({'categories':[c.name for c in categories]})


class AnalyzeListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class AnalyzeListAPI(generics.ListCreateAPIView):
    queryset = Analyze.objects.all()
    serializer_class = AnalyzeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = AnalyzeListPagination


class AnalyzeListUpdateAPI(generics.RetrieveUpdateAPIView):
    queryset = Analyze.objects.all()
    serializer_class = AnalyzeSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)


class AnalyzeListDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Analyze.objects.all()
    serializer_class = AnalyzeSerializer
    permission_classes = (IsAdminOrReadOnly,)





