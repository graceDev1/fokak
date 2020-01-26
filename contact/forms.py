from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nom', 'class': 'form-control'}), required=True)
    email = forms.EmailField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'E-mail', 'class': 'form-control'}), required=True)
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message', 'class': 'form-control'}), required=True)