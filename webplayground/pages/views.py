from django.views.generic import ListView, DetailView, CreateView
from .models import Page

class PageListView(ListView):
    model = Page
    template_name = 'pages/pages.html'
    context_object_name = 'pages'


class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/page.html'
    context_object_name = 'page'

class PageCreateView(CreateView):
    model = Page
    template_name = 'pages/page_form.html'
    fields = ['title','content','order']
    success_url = '/pages/'