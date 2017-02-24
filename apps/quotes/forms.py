from django import forms
from django.forms import widgets
from .models import Quote
from django.utils.translation import ugettext_lazy as _

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['author', 'message']
        labels = {
            'author': _('Quoted By')
        }
        widgets = {
          'message': forms.Textarea(attrs={'rows': 2, 'cols': 40})
          }
