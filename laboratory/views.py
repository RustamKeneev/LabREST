from django.shortcuts import render
from django.views.generic import ListView
from analyze.models import Analyze


class AnalyzeWithLaboratory(ListView):
    def get(self, request, *args, **kwargs):
        analyze_list = (Analyze.objects.filter(title=kwargs['id']))
        print(analyze_list)
        return render(request, '', context={
            analyze_list: 'analyze_list'
        })
