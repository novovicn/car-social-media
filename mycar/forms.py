from django import forms 
from .models import MyCar, Comment




class MyCarForm(forms.ModelForm):
    class Meta():
        model = MyCar
        fields = ('category','brand','model','image','owner','year')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        