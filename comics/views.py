from django.core import paginator
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required

from .models import ComicSeries

# Create your views here.

@login_required
def comics_home(request):
    page = request.GET.get('page', 1)
    all_comics = ComicSeries.objects.all().order_by('-last_update')
    paginator = Paginator(all_comics, 20)
    try:
        all_comics = paginator.page(page)
    except EmptyPage:
        all_comics = paginator.page(paginator.num_pages)
    
    context = {'all_comics': all_comics}

    return render(
        request, template_name='comics/comics_home.html',
        context=context
    )
