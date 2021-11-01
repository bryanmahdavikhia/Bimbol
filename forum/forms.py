from django.forms import widgets
from .models import Forum, Reply
from django import forms

class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ('title', 'desc')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': "title", 'placeholder': "Enter title"}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'rows': "10", 'id': "desc", 'placeholder': "Description..."}),
        }
    
class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('desc', )
        widgets = {
            'desc': forms.Textarea(attrs={'class': 'form-control', 'rows': "10", 'id': "desc", 'placeholder': "Write reply..."}),
        }

class ReplyofReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('desc', )
        widgets = {
            'desc': forms.Textarea(attrs={'class': 'form-control', 'rows': "2", 'id': "desc", 'placeholder': "Write reply..."}),
        }
