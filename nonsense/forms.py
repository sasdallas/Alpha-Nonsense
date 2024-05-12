from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    md = forms.CharField(required=True,
                        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Post something...",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",)

    class Meta:
        model = Post
        # I need to keep certain things hidden
        
        exclude = ("tuser", "author", "timestamp", "pst_id", "upvotes", "comments", "flags", )