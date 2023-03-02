from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'misc/about.html'


class ContactView(TemplateView):
    template_name = 'misc/contact.html' 