from django.urls import path
from analyze.views import *

urlpatterns = [
    path('analyze/list/', AnalyzeHome.as_view())
]