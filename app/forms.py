from django import forms

class QuoteForm(forms.Form):
    author = forms.CharField( max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Author'}), required=False )
    quote = forms.CharField( widget=forms.Textarea(attrs={'class':'form-control autogrow-target', 'placeholder':'Quote'}) )
    comment = forms.CharField( widget=forms.Textarea(attrs={'class':'form-control autogrow-target', 'placeholder':'Comment'}), required=False )



