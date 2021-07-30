from django.db import models
from django.forms import ModelForm

from .models import (
    ComicSeries, ComicIssue, Comment,
    IssuePanel
)


class ComicSeriesForm(ModelForm):
    class Meta:
        model = ComicSeries
        fields = fields = [
            'title', 'cover', 'description',
            'other_artists', 'com_category',
            'com_type'
        ]


class ComicIssueForm(ModelForm):
    class Meta:
        model = ComicIssue
        fields = [
            'issue', 'issue_title', 'issue_cover',
            'issue_description', 
        ]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


class IssuePanelForm(ModelForm):
    class Meta:
        model = IssuePanel
        fields = '__all__'
