from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

from .models import ComicSeries, ComicIssue
from .forms import ComicSeriesForm

def create_series(request):
    if request.method == 'POST':
        series_form = ComicSeriesForm(request.POST or None, request.FILES or None)

        if series_form.is_valid():
            print (series_form)
            series_obj = series_form.save(commit=False)
            series_obj.creator = request.user
            series_obj.last_update = timezone.now()
            series_obj.save()
            return redirect(
                'comics:view_series', slug= series_obj.slug,
                pk=series_obj.pk
            )
    
    else:
        series_form = ComicSeriesForm(request.POST or None, request.FILES or None)
    
    context = {
        'series_form': series_form
    }

    return render(
        request, template_name='comics/series_form.html',
        context=context
    )

def update_series(request, pk, slug):
    series = get_object_or_404(ComicSeries, pk=pk)
    series_form = ComicSeriesForm(
        request.POST or None, instance=series
    )

    if series_form.is_valid():
        series_obj = series_form.save(commit=False)
        series_obj.last_update = timezone.now()
        series_obj.save()
        return redirect(
            'comics:view_series', slug= series_obj.slug,
            pk=series_obj.pk
        )
    
    context = {
        'series_form': series_form
    }

    return render(
        request, template_name='comics/series_form.html',
        context=context
    )

def view_series(request, pk, slug):
    series = get_object_or_404(ComicSeries, pk=pk)
    issues = ComicIssue.objects.filter(issue=series.id).select_related()
    issue_count = ComicIssue.objects.filter(issue=series.id).select_related().count()

    context = {
        'series': series,
        'issues': issues,
        'count': issue_count
    }

    return render(
        request, template_name='comics/view_series.html',
        context=context
    )

def delete_series(request, pk, slug):
    series = get_object_or_404(ComicSeries, pk=pk)

    if request.method == 'POST':
        series.delete()
        return redirect('comics:comics_home')
    
    return render(
        request, template_name='comics/delete_series.html',
        context={}
    )
