from django.shortcuts import render
from policy.models import Policy
from django.http import HttpResponse


def index(request):
    posts = Policy.objects.all()
    context = {
        'posts': posts,
        'title': 'Конфициадальность'
    }
    return render(request, 'policy/policy.html', context=context)