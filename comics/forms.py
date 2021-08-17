from django import forms
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
        widgets = {
            'title': forms.TextInput(attrs={
                'id': 'title',
                'class': 'form-control'
            }),
            'cover': forms.FileInput(attrs={
                'id': 'cover',
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'id': 'description',
                'class': 'form-control'
            }),
            'other_artists': forms.TextInput(attrs={
                'id': 'other-artists',
                'class': 'form-control'
            }),
            'com_category': forms.Select(attrs={
                'id': 'category',
                'class': 'form-control'
            }),
            'com_type': forms.Select(attrs={
                'id': 'type',
                'class': 'form-control'
            })
        }


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
