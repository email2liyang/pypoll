from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(required=True,max_length=4)
    email = forms.EmailField(required=False)
    message = forms.CharField(required=True,widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message)
        if num_words < 3:
            raise forms.ValidationError("not enouth words")
        return message