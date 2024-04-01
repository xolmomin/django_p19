from django.shortcuts import render

from apps.models import Advisor


def index_view(request):
    context = {
        'advisors': Advisor.objects.all()
    }
    return render(request, 'apps/index.html', context)
