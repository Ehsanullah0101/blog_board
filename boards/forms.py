from django import forms
from .models import Topic, Post


class newTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'placeholder': "Whats on your mind?"}
                                                    ), max_length=4000, help_text="Max 4000 letters are allowed")

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class newPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', 'topic', 'created_by', 'update_by']
