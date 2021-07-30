from django.shortcuts import redirect, render, get_object_or_404
from django.template.defaultfilters import time
from django.utils import timezone

from .models import ComicSeries, ComicIssue, Comment, IssuePanel
from .forms import ComicIssueForm, IssuePanelForm, CommentForm

def create_issue(request, s_pk, pk, slug):
    issue_form = ComicIssueForm(request.POST or None)

    if issue_form.is_valid():
        issue_obj = issue_form.save(commit=False)
        issue_obj.creator = request.user
        issue_obj.series = ComicSeries.objects.get(pk=s_pk)
        issue_obj.date_uploaded = timezone.now()
        issue_obj.series.last_update = timezone.now()
        issue_obj.save()
        """
        remember to forward this view to panel upload
        """
        return None
    
    context = {
        'issue_form': issue_form
    }

    return render(
        request, template_name='comics/issue_form.html',
        context=context
    )

def update_issue(request, s_pk, pk, slug):
    issue = get_object_or_404(ComicIssue, pk=pk)
    issue_form = ComicIssueForm(
        request.POST or None, instance=issue
    )

    if issue_form.is_valid():
        issue_obj = issue_form.save(commit=False)
        issue_obj.series.last_update = timezone.now()
        issue_obj.save()
        return None
    
    context = {
        'issue_form': issue_form
    }

    return render(
        request, template_name='comics/issue_form.html',
        context=context
    )

def upload_panel(request, s_pk, pk, slug):
    pass

def view_issue(request, s_pk, pk, slug):
    series = ComicSeries.objects.get(pk=str(s_pk))
    issue = get_object_or_404(ComicIssue, pk=pk)
    panels = IssuePanel.objects.filter(issue=issue.pk).select_related()
    comments = Comment.objects.filter(issue=issue.pk).select_related()
    comment_form = CommentForm(request.POST or None)

def create_comment(request, s_pk, pk, slug):
    form = CommentForm(request.POST or None)

