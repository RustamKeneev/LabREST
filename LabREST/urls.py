"""LabREST URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

import laboratory
from LabREST import settings
from analyze.views import AnalyzeAPIView, AnalyzeAPILists, AnalyzeAPIUpdate, AnalyzeAPIIDetalView, AnalyzeViewSet, \
    AnalyzeListAPI, AnalyzeListUpdateAPI, AnalyzeListDestroyAPI, CategoryListAPI
from rest_framework import routers
from laboratory.views import AnalyzeWithLaboratory
from policy.views import index

router = routers.SimpleRouter()
router.register(r'analyzes', AnalyzeViewSet)

defaultRouter = routers.DefaultRouter()
defaultRouter.register(r'analyzesdefault', AnalyzeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('policy/', include('policy.urls')),
    path('api/v1/analyze/', AnalyzeAPIView.as_view()),
    path('api/v1/analyzeapilist/', AnalyzeAPILists.as_view()),
    path('api/v1/analyzeapilistsetviews/', AnalyzeViewSet.as_view({'get': 'list'})),
    path('api/v1/', include(router.urls)),
    # path('api/v1/analyzewithlaboratory', AnalyzeWithLaboratory.as_view()),
    path('api/v1/analyzewithlaboratory/', include('laboratory.urls')),
    path('api/v1/', include(defaultRouter.urls)),
    path('api/v1/analyzeapilist', AnalyzeListAPI.as_view()),
    path('api/v1/categoryapilist', CategoryListAPI.as_view()),
    path('api/v1/analyzeapiupdate/<int:pk>/', AnalyzeListUpdateAPI.as_view()),
    path('api/v1/analyzeapidelete/<int:pk>/', AnalyzeListDestroyAPI.as_view()),
    path('api/v1/analyzeapiupdatesetviews/<int:pk>/', AnalyzeViewSet.as_view({'put': 'update'})),
    path('api/v1/analyzeapiupdate/<int:pk>/', AnalyzeAPIUpdate.as_view()),
    path('api/v1/analyzeapidetail/<int:pk>/', AnalyzeAPIIDetalView.as_view()),
    path('api/v1/analyze/<int:pk>/', AnalyzeAPIView.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # url(r'^auth/', include('djoser.urls')),
    # url(r'^auth/', include('djoser.urls.authtoken')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)