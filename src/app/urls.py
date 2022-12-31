from django.urls import path, include

from rest_framework import routers

from . import views

#
# router = routers.SimpleRouter()
# router.register(r'articles', views.MyViewSet)


urlpatterns = [
    # path('api/v1/', include(router.urls)),

    # path('articles/', views.MyApiView.as_view()),

    path('', views.MyApiViewList3.as_view()),
    path('<int:pk>/', views.MyApiViewDetail3.as_view()),
    path('<int:pk>/update/', views.MyApiViewUpdate3.as_view()),
    path('<int:pk>/delete/', views.MyApiDeleteView3.as_view()),
]
