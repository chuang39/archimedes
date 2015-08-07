from django.views.generic import CreateView
from django.core.urlresolvers import reverse
from django.contrib import messages

from .models import Contact
from .forms import ContactForm

class ContactFormView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'

    def get_success_url(self, instance=None):
        messages.success(self.request, u'Message is received. We will contact you soon!')
        return reverse('contact.views.contact_form_view')

contact_form_view = ContactFormView.as_view()