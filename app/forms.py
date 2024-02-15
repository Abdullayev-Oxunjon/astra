from django import forms

from app.models import Subscribe


class SubscribeForm(forms.ModelForm):

    class Meta:
        model = Subscribe
        fields = ('email',)
