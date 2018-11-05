from django.forms import ModelForm
from myblog.models import Post


class AddPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'category']