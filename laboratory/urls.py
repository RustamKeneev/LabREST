from django.urls import path
from laboratory.views import *

urlpatterns = [
    path('analyze/laboratory/', AnalyzeWithLaboratory.as_view)
]