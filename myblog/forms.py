from django.forms import ModelForm
from myblog.models import Post


class AddPost(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
