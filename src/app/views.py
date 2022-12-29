from rest_framework import generics, views, viewsets, decorators
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from . import models, serializers, permissions


class MyViewSet(viewsets.ModelViewSet):
    queryset = models.Article.objects.all()
    serializer_class = serializers.MySerializer

    @decorators.action(methods=['get'], detail=False)
    def categories(self, request):
        categories = models.Category.objects.all()
        categories_names = [category.name for category in categories]
        return Response(categories_names)


# class MyApiView(generics.ListAPIView):
#     queryset = models.Article.objects.all()
#     serializer_class = serializers.MySerializer
#
#
# class MyApiView2(views.APIView):
#     def get(self, request):
#         queryset = models.Article.objects.all()
#         posts = serializers.MySerializer2(queryset, many=True).data
#         return Response({'posts': posts})
#
#     def post(self, request):
#         serializer = serializers.MySerializer2(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         new_post = serializer.data
#         return Response({'post': new_post})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response('pk = None !!!')
#
#         try:
#             instance = models.Article.objects.get(pk=pk)
#         except:
#             return Response('Статьи с таким pk не найдено')
#
#         serializer = serializers.MySerializer2(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         updated_post = serializer.data
#
#         return Response({'post': updated_post})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response('pk = None !!!')
#
#         try:
#             instance = models.Article.objects.get(pk=pk)
#         except:
#             return Response('Статьи с таким pk не найдено')
#
#         instance.delete()
#         return Response('Статья удалена успешно!')
#
#
class MyApiViewList3(generics.ListCreateAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.MySerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)


class MyApiViewDetail3(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.MySerializer
    permission_classes = (permissions.IsOwnerOrReadOnly,)


class MyApiViewUpdate3(generics.RetrieveUpdateAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.MySerializer
    permission_classes = (permissions.IsOwnerOrReadOnly,)


class MyApiDeleteView3(generics.RetrieveDestroyAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.MySerializer
    permission_classes = (permissions.IsAdminOrReadOnly,)
