from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

    #@method_decorator(ensure_csrf_cookie)
    #def dispatch(self, *args, **kwargs):
    #    return super(IndexView, self).dispatch(*args, **kwargs)

class AboutusView(TemplateView):
    template_name = 'about_us.html'