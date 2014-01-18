from django import forms
from app.models import *

class QuoteForm(forms.Form):
    quote_id = forms.IntegerField( widget=forms.HiddenInput(attrs={'class':'quote_id'}), required=False )
    author = forms.CharField( max_length=255, widget=forms.TextInput(attrs={'class':'form-control quote_author', 'placeholder':'Author'}), required=False )
    quote = forms.CharField( widget=forms.Textarea(attrs={'class':'form-control autogrow-target quote_quote', 'placeholder':'Quote'}) )
    comment = forms.CharField( widget=forms.Textarea(attrs={'class':'form-control autogrow-target quote_comment', 'placeholder':'Comment'}), required=False )

