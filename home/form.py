from django import forms
# from froala_editor.widgets import FroalaEditor
from .models import *
from markdownx.fields import MarkdownxFormField

class BlogForm(forms.ModelForm):
    content = MarkdownxFormField()
    class Meta:
        model = BlogModel
        fields = ['title', 'content']
