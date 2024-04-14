from django import forms
from .models import BugReport, FeatureRequest


class BugReportForm(forms.ModelForm):
    class Meta:
        model = BugReport
        fields = ['title', 'description', 'project', 'task', 'status', 'priority']


class FeatureRequestForm(forms.ModelForm):
    class Meta:
        model = FeatureRequest
        fields = ['title', 'description', 'project', 'task', 'status', 'priority']


class FeedbackForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100)
    email = forms.EmailField(label='Электронная почта')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')
