from django.shortcuts import render

from comics.models import (
    ComicSeries, ComicCategory, ComicType
)

# Create your views here.

def home(request):
    series = ComicSeries.objects.all().order_by('-last_update')[:5]
    categories = ComicCategory.objects.all()
    comic_types = ComicType.objects.all()

    context = {
        'series': series,
        'categories': categories,
        'types': comic_types
    }

    return render(
        request, template_name='home/home.html',
        context=context
    )
