# -*- coding: utf-8 -*-  
from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': "名字*",
                'class':"input__field input__field--jiro",
                'type':"text",
            }),
            'email': forms.TextInput(attrs={
                'placeholder': "邮箱*",
                'class':"input__field input__field--jiro",
                'type':"email",
            }),
            'url': forms.TextInput(attrs={
                'placeholder': "网址",
                'class':"input__field input__field--jiro",
                'type':"url",
            }),
            'text': forms.Textarea(attrs={
                'placeholder': '我来评两句~',
                'class':"input-block-level comt-area",
            }),
        }
