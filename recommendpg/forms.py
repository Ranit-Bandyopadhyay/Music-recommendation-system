from django import forms


class ArtistForm(forms.Form):
    artist = forms.CharField(max_length=100)

#class ContactForm(forms.Form):
#    name = forms.CharField(max_length=30)
#    email = forms.EmailField(max_length=254)
#    message = forms.CharField(
#        max_length=2000,
#        widget=forms.Textarea(),
#        help_text='Write here your message!'
#    )
#    source = forms.CharField(       # A hidden input for internal use
#        max_length=50,              # tell from which page the user sent the message
#        widget=forms.HiddenInput()
#    )