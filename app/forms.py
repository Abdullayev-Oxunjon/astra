from django import forms

from app.models.blog import BlogComment
from app.models.other import Contact
from app.models.rooms import Booking
from app.models.services import Subscribe


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ('email',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ('name', 'email', 'message')


class BookingModelForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
