from django.views.generic.base import TemplateView
from django.views.generic.base import TemplateView
from archimedes.forms import ContactForm
from django.views.generic.edit import FormView

from django.shortcuts import render

import boto.sns

class IndexView(TemplateView):
    template_name = 'index.html'

    #@method_decorator(ensure_csrf_cookie)
    #def dispatch(self, *args, **kwargs):
    #    return super(IndexView, self).dispatch(*args, **kwargs)

class AboutusView(TemplateView):
    template_name = 'about_us.html'

class SolutionsView(TemplateView):
    template_name = 'solutions.html'

class SolutionA150View(TemplateView):
    template_name = 'solution_A150.html'

class ProductsView(TemplateView):
    template_name = 'products.html'

class NewsView(TemplateView):
    template_name = 'news.html'

"""
class ContactView(TemplateView):
    template_name = 'contact.html'
    form_class = ContactForm

    def post(self, request, *args, **kwargs):
        form = (request.POST)

        import pdb; pdb.set_trace()
        print("12313131")


        return render(request, self.template_name, {'form': form})
"""
def contact(request):

    form = ContactForm(request.POST or None)
    if form.is_valid():
        print form.cleaned_data
        regions = boto.sns.regions()
        print regions
        sns = boto.sns.SNSConnection(aws_access_key_id='AKIAJXN4QBOQO6TR7T5Q',
                                aws_secret_access_key='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',
                                region=u'us-west-2')

        print "=====",sns

        sns.publish(u'arn:aws:sns:us-west-2:451326512542:ArchimedesCustomerContactTopic', '123', 'sdfasfda')


    context = {'form': form}
    return render(request, 'contact.html', context)

