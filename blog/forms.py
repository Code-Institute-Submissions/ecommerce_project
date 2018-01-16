from django import forms
from .models import Post, Comment, Newsletter

class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = ( 'title', 'content', 'image',)
       
class CommentsForm(forms.ModelForm):
   class Meta:
       model = Comment
       fields = ( 'title', 'content')  
       
class MakePaymentForm(forms.Form):
    
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2018, 2036)]
 
    credit_card_number = forms.CharField(label='Credit card number', required='False')
    cvv = forms.CharField(label='Security code (CVV)', required='False')
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES, required='False')
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES, required='False')
    stripe_id = forms.CharField(widget=forms.HiddenInput)
       
class NewsletterForm(forms.ModelForm):
   class Meta:
       model = Newsletter
       fields = ( 'full_name', 'email', 'address_line_1', 'address_line_2', 'town_or_city', 'country')   
 