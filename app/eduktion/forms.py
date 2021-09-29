from django import forms


class ContactForm(forms.Form):
    Name = forms.CharField()
    Subject = forms.CharField()
    Email = forms.EmailField(label="Email:", required=True)
    message = forms.Textarea();
