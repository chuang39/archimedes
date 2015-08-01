from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Name")
    email = forms.EmailField(label="Email")
    company = forms.CharField(label="Company", required=False)
    phone = forms.CharField(label="Phone")
    message = forms.CharField(label="Body", widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass