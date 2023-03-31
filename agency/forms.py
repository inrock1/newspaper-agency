from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from agency.models import Redactor, Newspaper


class NewspaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Newspaper
        fields = "__all__"


class NewspaperSearchForm(forms.Form):
    model = forms.CharField(max_length=255, required=False)


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + ("years_of_experience",)


class RedactorSearchForm(forms.Form):
    username = forms.CharField(max_length=255, required=False)


class TopicSearchForm(forms.Form):
    name = forms.CharField(max_length=255, required=False)
