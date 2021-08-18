from django.core import paginator
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required

from .models import ComicCategory, ComicSeries, ComicType
from .forms import CategoryForm, TypeForm

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

@login_required
def create_category(request):
    form = CategoryForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('comics:all_categories')
    
    return render(
        request, template_name='comics/categories/category_form.html',
        context={'form': form}
    )

def categories_list(request):
    categories = ComicCategory.objects.all().order_by('cat_name')

    return render(
        request, template_name='comics/categories/all_categories.html',
        context={'categories': categories}
    )

def view_category(request, pk):
    category = get_object_or_404(ComicCategory, pk=pk)
    comics = ComicSeries.objects.filter(com_category=category.id).select_related().order_by('-last_update')
    
    context = {
        'category': category,
        'comics': comics
    }
    return render(
        request, 'comics/categories/category.html',
        context=context
    )

@login_required
def create_type(request):
    form = TypeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('comics:all_types')
    
    return render(
        request, 'comics/types/type_form.html',
        context={'form': form}
    )

def types_list(request):
    types = ComicType.objects.all().order_by('type_name')
    
    return render(
        request, template_name='comics/types/all_types.html',
        context={'types': types}
    )


def view_type(request, pk):
    comic_type = get_object_or_404(ComicType, pk=pk)
    comics = ComicSeries.objects.filter(com_type=comic_type.id).select_related().order_by('-last_update')

    context = {
        'type': comic_type,
        'comics': comics
    }
    return render(
        request, template_name='comics/types/type.html',
        context=context
    )
