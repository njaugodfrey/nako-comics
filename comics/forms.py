from django.db import models
from django.forms import ModelForm

from .models import (
    ComicSeries, ComicIssue, Comment,
    IssuePanel
)


class ComicSeriesForm(ModelForm):
    class Meta:
        model = ComicSeries
        fields = '__all__'


class ComicIssueForm(ModelForm):
    class Meta:
        model = ComicIssue
        fields = '__all__'


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


class IssuePanelForm(ModelForm):
    class Meta:
        model = IssuePanel
        fields = '__all__'
