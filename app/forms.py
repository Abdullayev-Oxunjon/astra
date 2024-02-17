from django import forms

from app.models import Subscribe, Contact, BlogComment, Booking


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
